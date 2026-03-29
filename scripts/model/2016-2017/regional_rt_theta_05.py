from pathlib import Path
import os
from scipy.stats import nbinom
import numpy as np
import matplotlib.pyplot as pt
import time
import pandas as pd


CASE_DIR = Path("data/processed/cases")
GAMMA_DIR = Path("results/mobility/2016_2017/0.5")
BETA_OUT_DIR = Path("results/model/2016_2017/0.5/beta")
RT_OUT_DIR = Path("results/model/2016_2017/0.5/rt")
FIG_OUT_DIR = Path("results/figures/model/2016_2017/0.5")

N_PARTICLES = int(os.getenv("N_PARTICLES", "1000000"))


def moving_average(x, w):
    x = np.asarray(x, dtype=float)
    kernel = np.ones(w)

    num = np.convolve(x, kernel, mode="same")
    den = np.convolve(np.ones(len(x)), kernel, mode="same")

    return num / den


def transform_datetype(df):
    df["date"] = pd.to_datetime(df["date"])
    return df


def RK4(S, I, R, beta, xi, Ntot, sigma, dt):
    kS1 = -xi * beta * S * I / Ntot
    kI1 = (xi * beta * S * I / Ntot) - sigma * I
    kR1 = sigma * I

    kS2 = -xi * beta * (S + 0.5 * kS1 * dt) * (I + 0.5 * kI1 * dt) / Ntot
    kI2 = (xi * beta * (S + 0.5 * kS1 * dt) * (I + 0.5 * kI1 * dt) / Ntot) - sigma * (I + 0.5 * kI1 * dt)
    kR2 = sigma * (I + 0.5 * kI1 * dt)

    kS3 = -xi * beta * (S + 0.5 * kS2 * dt) * (I + 0.5 * kI2 * dt) / Ntot
    kI3 = (xi * beta * (S + 0.5 * kS2 * dt) * (I + 0.5 * kI2 * dt) / Ntot) - sigma * (I + 0.5 * kI2 * dt)
    kR3 = sigma * (I + 0.5 * kI2 * dt)

    kS4 = -xi * beta * (S + kS3 * dt) * (I + kI3 * dt) / Ntot
    kI4 = (xi * beta * (S + kS3 * dt) * (I + kI3 * dt) / Ntot) - sigma * (I + kI3 * dt)
    kR4 = sigma * (I + kI3 * dt)

    S = S + (kS1 + 2.0 * kS2 + 2.0 * kS3 + kS4) / 6.0
    I = I + (kI1 + 2.0 * kI2 + 2.0 * kI3 + kI4) / 6.0
    R = R + (kR1 + 2.0 * kR2 + 2.0 * kR3 + kR4) / 6.0
    confirm = (kR1 + 2.0 * kR2 + 2.0 * kR3 + kR4) / 6.0

    return np.array([S, I, R, confirm])


def run_region(
    region_name,
    case_filename,
    gamma_filename,
    beta_csv_filename,
    rt_csv_filename,
    beta_png_filename,
    n_tot,
    color,
    use_gamma=True,
):
    scale = 1
    window = 7
    Ntot = n_tot
    dt = 1.0
    cases = N_PARTICLES
    sigma = 1.0 / 4.1
    beta_s = 0.15

    BETA_OUT_DIR.mkdir(parents=True, exist_ok=True)
    RT_OUT_DIR.mkdir(parents=True, exist_ok=True)
    FIG_OUT_DIR.mkdir(parents=True, exist_ok=True)

    # xi
    if use_gamma:
        gamma_path = GAMMA_DIR / gamma_filename
        df_gamma = pd.read_csv(gamma_path)
        if "gamma" not in df_gamma.columns:
            raise ValueError(f"{gamma_path} must contain a 'gamma' column.")
        xi = df_gamma["gamma"]
    else:
        xi = 1

    np.random.seed()
    start = time.time()

    # CSV 읽기
    data = pd.read_csv(CASE_DIR / case_filename)
    data = transform_datetype(data)

    # cases 열만 숫자로 변환
    data["cases"] = pd.to_numeric(data["cases"], errors="coerce")

    # 숫자로 변환 안 되는 값 제거
    data = data.dropna(subset=["cases"]).reset_index(drop=True)

    # 원본 cases 배열
    cases_array = data["cases"].to_numpy(dtype=float)

    # moving average 적용
    region_cases = moving_average(cases_array, window)

    # Particle filter Rt
    day = len(region_cases)

    if day == 0:
        raise ValueError(f"{region_name}: no valid case observations were found in {case_filename}.")
    if not np.isscalar(xi) and len(xi) < day:
        raise ValueError(
            f"{region_name}: gamma series in {gamma_filename} has length {len(xi)}, "
            f"but at least {day} rows are required."
        )

    dates = pd.to_datetime(data["date"])
    plot_date = dates[0:]

    # Initial condition and beta
    random_numbers = np.random.normal(0, beta_s, cases * day)
    normal_beta = np.reshape(random_numbers, (day, cases))

    Pf_S = np.zeros([day + 1, cases])
    Pf_I = np.zeros([day + 1, cases])
    Pf_R = np.zeros([day + 1, cases])
    Pf_beta = np.zeros([day + 1, cases])

    rv_index = np.zeros([day + 1, cases], dtype=int)
    Pf_confirm = np.zeros([day, cases])
    confirm = np.zeros(day)
    Pf_RPN = np.zeros(day)
    tm = np.zeros(day)

    lambda_i = region_cases[0]

    Pf_I[0, :] = np.random.poisson(lambda_i, size=cases)
    Pf_S[0, :] = Ntot - Pf_I[0, :] - Pf_R[0, :]
    Pf_beta[0, :] = 1.05 * np.exp(normal_beta[0, :]) * sigma * Ntot / Pf_S[0, :]

    n = 40

    # time evolution
    for k in range(day):
        tm[k] = k

        Pf_beta[k + 1, :] = Pf_beta[k, :] * np.exp(normal_beta[k, :])
        xi_k = xi if np.isscalar(xi) else xi.iloc[k]
        Pf_results = RK4(Pf_S[k, :], Pf_I[k, :], Pf_R[k, :], Pf_beta[k + 1, :], xi_k, Ntot, sigma, dt)

        Pf_S[k + 1, :] = Pf_results[0]
        Pf_I[k + 1, :] = Pf_results[1]
        Pf_R[k + 1, :] = Pf_results[2]
        Pf_confirm[k, :] = Pf_results[3]

        weight = nbinom.pmf(round(region_cases[k]), n, n / (Pf_confirm[k, :] + n))

        weight_sum = np.sum(weight)
        if weight_sum == 0 or not np.isfinite(weight_sum):
            weight = np.ones(cases) / cases
        else:
            weight = weight / weight_sum

        random_list = np.random.choice(np.arange(cases), size=cases, replace=True, p=weight)
        rv_index[k + 1, :] = random_list

        Pf_S[k + 1, :] = Pf_S[k + 1, random_list]
        Pf_I[k + 1, :] = Pf_I[k + 1, random_list]
        Pf_R[k + 1, :] = Pf_R[k + 1, random_list]
        Pf_beta[k + 1, :] = Pf_beta[k + 1, random_list]

    xi_for_pf = xi if np.isscalar(xi) else xi.to_numpy()
    Pf_RPN = xi_for_pf * (np.mean(Pf_beta[1:, :], axis=1) / sigma) / (np.mean(Pf_S[1:, :], axis=1) / Ntot)
    region_confirm = np.mean(Pf_confirm, axis=1)

    # Particle smoother Rt
    Ps_S = np.zeros([day + 1, cases])
    Ps_beta = np.zeros([day + 1, cases])
    Ps_RPN = np.zeros(day)

    Ps_Pf = np.arange(cases)
    Ps_beta[day, :] = Pf_beta[day, Ps_Pf]

    Ps_Pf = rv_index[day, Ps_Pf]
    Ps_beta[day - 1, :] = Pf_beta[day - 1, Ps_Pf]

    for k in range(day - 2, -1, -1):
        Ps_Pf = rv_index[k + 1, Ps_Pf]
        Ps_beta[k, :] = Pf_beta[k, Ps_Pf]

    Rt = xi_for_pf * (np.mean(Ps_beta[1:, :], axis=1) / sigma) / (np.mean(Pf_S[1:, :], axis=1) / Ntot)
    beta = np.mean(Ps_beta[1:, :], axis=1)

    beta_t = pd.DataFrame({"date": dates[0:], "beta": beta[0:]})
    beta_t.to_csv(BETA_OUT_DIR / beta_csv_filename, index=False)

    Rt_t = pd.DataFrame({"date": dates[0:], "rt": Rt[0:]})
    Rt_t.to_csv(RT_OUT_DIR / rt_csv_filename, index=False)

    # Rt Plot
    pt.figure()
    pt.plot(plot_date[10:], Rt[10:], linestyle="-", linewidth=1.5, color=color, label="$R_t$")
    pt.title(f"{region_name} Rt")
    pt.legend(loc=0)
    pt.xlabel("Date")
    pt.yticks([0.4, 0.8, 1.2, 1.6, 2.0, 2.4])
    pt.show()

    # beta Plot
    pt.figure()
    pt.plot(plot_date[10:], beta[10:], linestyle="-", linewidth=1.5, color=color, label="beta")
    pt.title(f"{region_name} beta")
    pt.legend(loc=0)
    pt.xlabel("Date")
    pt.savefig(FIG_OUT_DIR / beta_png_filename, format="png", bbox_inches="tight")
    pt.show()

    # cases Plot
    pt.figure()
    pt.plot(plot_date, region_cases, linestyle="-", linewidth=1.5, color=color, label=f"{region_name}_cases")
    pt.plot(plot_date, region_confirm, linestyle="--", linewidth=1.5, color=color, label=f"{region_name}_Confirmation")
    pt.legend(loc=0)
    pt.title("Confirmation")
    pt.xlabel("Date")
    pt.tight_layout()
    pt.show()

    print(f"{region_name} elapsed time:", time.time() - start)

    return {
        "dates": dates,
        "plot_date": plot_date,
        "cases": region_cases,
        "confirm": region_confirm,
        "Rt": Rt,
        "beta": beta,
    }


def main():
    BETA_OUT_DIR.mkdir(parents=True, exist_ok=True)
    RT_OUT_DIR.mkdir(parents=True, exist_ok=True)
    FIG_OUT_DIR.mkdir(parents=True, exist_ok=True)

    # 대한민국
    korea = run_region(
        region_name="Korea",
        case_filename="Korea_cases.csv",
        gamma_filename="Seoul_gamma.csv",
        beta_csv_filename="Korea_beta_0.5(2016~2017).csv",
        rt_csv_filename="Korea_rt_0.5(2016~2017).csv",
        beta_png_filename="Korea_beta.png",
        n_tot=51_737_380,
        color="#000000",
        use_gamma=False,
    )

    # 서울 
    seoul = run_region(
        region_name="Seoul",
        case_filename="Seoul_cases.csv",
        gamma_filename="Seoul_gamma.csv",
        beta_csv_filename="Seoul_beta_0.5(2016~2017).csv",
        rt_csv_filename="Seoul_rt_0.5(2016~2017).csv",
        beta_png_filename="Seoul_beta.png",
        n_tot=22_689_358.5,
        color="#D62728",
        use_gamma=True,
    )

    # 부산
    busan = run_region(
        region_name="Busan",
        case_filename="Busan_cases.csv",
        gamma_filename="Busan_gamma.csv",
        beta_csv_filename="Busan_beta_0.5(2016~2017).csv",
        rt_csv_filename="Busan_rt_0.5(2016~2017).csv",
        beta_png_filename="Busan_beta.png",
        n_tot=3_484_591,
        color="#1F77B4",
        use_gamma=True,
    )

    # 대전
    daejeon = run_region(
        region_name="Daejeon",
        case_filename="Daejeon_cases.csv",
        gamma_filename="Daejeon_gamma.csv",
        beta_csv_filename="Daejeon_beta_0.5(2016~2017).csv",
        rt_csv_filename="Daejeon_rt_0.5(2016~2017).csv",
        beta_png_filename="Daejeon_beta.png",
        n_tot=1_508_298.5,
        color="#2CA02C",
        use_gamma=True,
    )

    # 대구
    daegu = run_region(
        region_name="Daegu",
        case_filename="Daegu_cases.csv",
        gamma_filename="Daegu_gamma.csv",
        beta_csv_filename="Daegu_beta_0.5(2016~2017).csv",
        rt_csv_filename="Daegu_rt_0.5(2016~2017).csv",
        beta_png_filename="Daegu_beta.png",
        n_tot=2_479_894,
        color="#FF7F0E",
        use_gamma=True,
    )

    # 광주
    gwangju = run_region(
        region_name="Gwangju",
        case_filename="Gwangju_cases.csv",
        gamma_filename="Gwangju_gamma.csv",
        beta_csv_filename="Gwangju_beta_0.5(2016~2017).csv",
        rt_csv_filename="Gwangju_rt_0.5(2016~2017).csv",
        beta_png_filename="Gwangju_beta.png",
        n_tot=1_466_492,
        color="#9467BD",
        use_gamma=True,
    )

    plot_date = korea["plot_date"]

    # Regional Confirmation
    pt.figure(figsize=(10, 5))
    pt.plot(plot_date, korea["cases"], linestyle="-", linewidth=1.5, color="#000000", label="Korea_cases")
    pt.plot(plot_date, korea["confirm"], linestyle="--", linewidth=1.5, color="#000000", label="Korea_Confirm")
    pt.plot(plot_date, seoul["cases"], linestyle="-", linewidth=1.5, color="#D62728", label="Seoul_cases")
    pt.plot(plot_date, seoul["confirm"], linestyle="--", linewidth=1.5, color="#D62728", label="Seoul_Confirm")
    pt.plot(plot_date, busan["cases"], linestyle="-", linewidth=1.5, color="#1F77B4", label="Busan_cases")
    pt.plot(plot_date, busan["confirm"], linestyle="--", linewidth=1.5, color="#1F77B4", label="Busan_Confirm")
    pt.plot(plot_date, daejeon["cases"], linestyle="-", linewidth=1.5, color="#2CA02C", label="Daejeon_cases")
    pt.plot(plot_date, daejeon["confirm"], linestyle="--", linewidth=1.5, color="#2CA02C", label="Daejeon_Confirm")
    pt.plot(plot_date, daegu["cases"], linestyle="-", linewidth=1.5, color="#FF7F0E", label="Daegu_cases")
    pt.plot(plot_date, daegu["confirm"], linestyle="--", linewidth=1.5, color="#FF7F0E", label="Daegu_Confirm")
    pt.plot(plot_date, gwangju["cases"], linestyle="-", linewidth=1.5, color="#9467BD", label="Gwangju_cases")
    pt.plot(plot_date, gwangju["confirm"], linestyle="--", linewidth=1.5, color="#9467BD", label="Gwangju_Confirm")
    pt.legend(loc=0)
    pt.title("Regional_Confirmation")
    pt.xlabel("Date")
    pt.tight_layout()
    pt.savefig(FIG_OUT_DIR / "2016~2017_confirm.png", format="png", bbox_inches="tight")
    pt.show()

    # Regional beta
    colors = ["#000000", "#D62728", "#1F77B4", "#2CA02C", "#FF7F0E", "#9467BD", "#8C564B"]
    plot_dates = korea["dates"][10:]

    pt.figure()
    pt.plot(plot_dates, seoul["beta"][10:], "-", linewidth=1, color=colors[1], label="Seoul")
    pt.plot(plot_dates, busan["beta"][10:], "-", linewidth=1, color=colors[2], label="Busan")
    pt.plot(plot_dates, daejeon["beta"][10:], "-", linewidth=1, color=colors[3], label="Daejeon")
    pt.plot(plot_dates, daegu["beta"][10:], "-", linewidth=1, color=colors[4], label="Daegu")
    pt.plot(plot_dates, gwangju["beta"][10:], "-", linewidth=1, color=colors[5], label="Gwangju")
    pt.title("Regional beta")
    pt.legend(loc=0)
    pt.ylabel("beta")
    pt.xlabel("Date")
    pt.savefig(FIG_OUT_DIR / "2016~2017_0.5_beta.png", format="png", bbox_inches="tight")
    pt.show()

    # Regional Rt
    pt.figure()
    pt.plot(plot_dates, korea["Rt"][10:], linestyle="--", linewidth=1.5, color=colors[0], label="Korea")
    pt.plot(plot_dates, seoul["Rt"][10:], "-", linewidth=1, color=colors[1], label="Seoul")
    pt.plot(plot_dates, busan["Rt"][10:], "-", linewidth=1, color=colors[2], label="Busan")
    pt.plot(plot_dates, daejeon["Rt"][10:], "-", linewidth=1, color=colors[3], label="Daejeon")
    pt.plot(plot_dates, daegu["Rt"][10:], "-", linewidth=1, color=colors[4], label="Daegu")
    pt.plot(plot_dates, gwangju["Rt"][10:], "-", linewidth=1, color=colors[5], label="Gwangju")
    pt.title("Regional $R_t$ Comparison")
    pt.legend(loc=0)
    pt.yticks([0.4, 0.8, 1.2, 1.6, 2.0, 2.4])
    pt.axhline(1.0, linestyle="--", label="Reference ($R_t$ = 1)")
    pt.ylabel("$R_t$")
    pt.xlabel("Date")
    pt.savefig(FIG_OUT_DIR / "2016~2017_0.5_Rt.png", format="png", bbox_inches="tight")
    pt.show()


if __name__ == "__main__":
    main()
