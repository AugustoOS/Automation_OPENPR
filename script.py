import subprocess
import sys
import os
import local_config as cfg


def run_cmd(cmd, cwd=None, capture_output=False):
    result = subprocess.run(
        cmd,
        cwd=cwd,
        shell=True,
        text=True,
        capture_output=capture_output
    )
    if result.returncode != 0:
        print(f"Error during run: {cmd}")
        if result.stderr:
            print(result.stderr)
        sys.exit(1)
    return result.stdout.strip() if capture_output else None

def main():
    if len(sys.argv) != 2:
        print("Format: openpr <pr_url>")
        sys.exit(1)

    pr_url = sys.argv[1]

    # Check local repo path
    if not os.path.exists(cfg.REPO_PATH):
        print(f"Repo not found: {cfg.REPO_PATH}")
        sys.exit(1)

    # Fetch and Checkout to pr branch located in the pr
    run_cmd(f'gh pr checkout "{pr_url}"', cwd=cfg.REPO_PATH)

    # Geting files from PR: .slx and .sldd
    diff_output = run_cmd(f'gh pr diff "{pr_url}" --name-only', cwd=cfg.REPO_PATH, capture_output=True)
    model_files = [
        line for line in diff_output.splitlines()
        if line.endswith(".slx") or line.endswith(".sldd")
    ]

    if not model_files:
        print("No .slx or .sldd found in PR.")
        sys.exit(1)

    print("Found files:")
    for f in model_files:
        print(f" - {f}")
    
    # Add to path modules and submodules and classdef FCADataClasses.Parameter (Parameter.m)
    repo_for_matlab = cfg.REPO_PATH.replace("\\", "/")
    matlab_cmds = [
        f"addpath(genpath('{repo_for_matlab}')); ",
        "try, p = FCADataClasses.Parameter; "
        "catch ME, disp('Instance error: FCADataClasses.Parameter'); disp(getReport(ME)); end;"
    ]

    # Open each found file in matlab
    for rel_path in model_files:
        full_path = os.path.join(cfg.REPO_PATH, rel_path).replace("\\", "/")
        matlab_cmds.append(f"open('{full_path}');")

    matlab_code = " ".join(matlab_cmds)
    run_cmd(f'{cfg.MATLAB_2022b} -nosplash -r "{matlab_code}"')

if __name__ == "__main__":
    main()
