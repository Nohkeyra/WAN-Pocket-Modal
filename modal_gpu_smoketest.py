import subprocess
import time
import modal

app = modal.App("wan-pocket-gpu-smoketest")

@app.function()
@modal.fastapi_endpoint(method="GET")
def health():
    return {
        "ok": True,
        "service": "wan-pocket-gpu-smoketest",
        "gpu_requested": False,
    }

@app.function(gpu="T4", timeout=120)
@modal.fastapi_endpoint(method="GET")
def gpu():
    started = time.time()
    try:
        output = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=name,memory.total,driver_version",
                "--format=csv,noheader,nounits",
            ],
            text=True,
        ).strip()

        parts = [p.strip() for p in output.split(",")]
        return {
            "ok": True,
            "cloud_gpu": True,
            "provider": "Modal",
            "gpu_name": parts[0] if len(parts) > 0 else output,
            "memory_mb": int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else None,
            "driver_version": parts[2] if len(parts) > 2 else None,
            "elapsed_ms": round((time.time() - started) * 1000, 1),
            "note": "Inference did not run on your Android GPU.",
        }
    except Exception as e:
        return {
            "ok": False,
            "cloud_gpu": True,
            "provider": "Modal",
            "error": f"{type(e).__name__}: {e}",
        }
