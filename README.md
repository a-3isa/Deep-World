# Deep-World

A Django REST API that applies image effects with neural networks: DeepDream-style transformations and artistic style transfer.

## Endpoints

- `POST /` multipart: `image` (file), `style` (string). Runs the DeepDream script on the upload and returns the result URL.
- `POST /prism` multipart: `content` (file), `style` (file). Runs neural style transfer with Prism and returns the result URL.

Both responses look like `{ "result": "http://<host>:<port>/<file>" }`.

## Credits

Style transfer uses [Prism](https://github.com/moritztng/prism) by Moritz Thuening (MIT). `style_transfer/` is derived from it.

## Setup

Prerequisites: Python 3.7+, optionally a CUDA GPU.

```bash
git clone https://github.com/a-3isa/Deep-World
cd Deep-World
pip install django djangorestframework markdown django-filter tensorflow torch
python manage.py migrate
python manage.py runserver 0.0.0.0:599
```

`requirments.sh` lists the original install commands (including a CUDA 11.3 PyTorch build).

## Structure

```
deepdream/       Django project settings
dream/           API views and urls
style_transfer/  Prism code
test.py          DeepDream script (called by the API)
prism.py         style transfer script (called by the API)
baseline.py      TensorFlow style model runner
```

## Notes

This is an experiment, not production code: the views shell out to scripts with `os.system` and build result URLs from the host address in `ip.txt`. Run it only on a trusted network.

`ip.txt` is not committed. Create it with your machine's address, or run `ip_puller.py`, which writes your public IP to `ip.txt` and, if `DEPLOY_HOST` is set (for example `user@server`), copies it there with `scp` using your SSH key. Optional: `DEPLOY_PATH` (default `~/deepdream/`).
