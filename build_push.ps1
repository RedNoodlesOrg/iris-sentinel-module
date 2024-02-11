poetry build
wsl -d podman-machine-default -u root enterns podman cp /mnt/s/iris-sentinel-module/dist/iris_sentinel_module-0.1.0-py3-none-any.whl iriswebapp_worker:dependencies/iris_sentinel_module-0.1.0-py3-none-any.whl
podman exec -it iriswebapp_worker /bin/sh -c "pip3 install dependencies/iris_sentinel_module-0.1.0-py3-none-any.whl --force-reinstall"
podman restart iriswebapp_worker
wsl -d podman-machine-default -u root enterns podman cp /mnt/s/iris-sentinel-module/dist/iris_sentinel_module-0.1.0-py3-none-any.whl iriswebapp_app:dependencies/iris_sentinel_module-0.1.0-py3-none-any.whl
podman exec -it iriswebapp_app /bin/sh -c "pip3 install dependencies/iris_sentinel_module-0.1.0-py3-none-any.whl --force-reinstall"
podman restart iriswebapp_app iriswebapp_nginx