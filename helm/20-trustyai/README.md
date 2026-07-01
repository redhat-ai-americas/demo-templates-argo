# Trusty AI

If you want to use MLServer in conjunction with Trusty, you must use the Python version due to an incompatibility in the APIs: https://redhat.atlassian.net/browse/RHOAIENG-66469

Please note that the Python version is currently unsupported (as of RHOAI 3.4), so you will need to use a dev version and talk to the change of direction in Trusty. Note also that the Python version currently doesn't support a Database backend, so you will have to use a PVC.