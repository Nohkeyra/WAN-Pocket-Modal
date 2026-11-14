# WAN Pocket Modal GPU Deploy

This repo avoids installing Modal inside Termux.

Flow:
Android/Termux -> Git push -> GitHub Actions Ubuntu runner -> Modal deploy -> Modal T4 endpoint

## Required GitHub repository secrets
- MODAL_TOKEN_ID
- MODAL_TOKEN_SECRET

Create the API token in Modal Dashboard workspace settings.
Do not commit the token into this repository.

## Deploy
Push to main or run the workflow manually from GitHub Actions.

The workflow will:
1. use Ubuntu
2. install Python 3.11
3. install Modal 1.6.4
4. run `modal deploy modal_gpu_smoketest.py`

## Test from Termux
After Actions succeeds, copy the `gpu` *.modal.run URL from the deploy log:

bash test_gpu.sh 'https://YOUR-GPU-ENDPOINT.modal.run'
