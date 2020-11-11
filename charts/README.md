# Acceleration Helm Chart

This chart bootstraps an acceleration app on a [Kubernetes](http://kubernetes.io/) cluster using the [Helm](https://helm.sh) package manager.

## Requirements

- k8s
- nginx-ingress
- [Helm3](https://helm.sh)
- kubectl

## Installation

**Create namespace before running chart:**

```bash
kubectl create ns acceleration
```

Installation:

```bash
helm install -n acceleration acceleration ./charts/acceleration
```

## Environments

The env chart values are in directory `./charts/env`

### production installation

```bash
helm install -n acceleration acceleration -f ./charts/envs/production.yaml ./charts/acceleration
```

## Benchmarks

Tests were made using [wrk](https://github.com/wg/wrk)

```bash
wrk -t5 -c100 -d1h https://join-acceleration.1mr.me/calc\?vf\=200\&vi\=5\&t\=123 --latency
```

*Results*

```bash
Running 60m test @ https://join-acceleration.1mr.me/calc?vf=200&vi=5&t=123
  5 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   478.04ms  237.37ms   2.00s    69.18%
    Req/Sec    43.22     26.42   192.00     69.58%
  Latency Distribution
     50%  456.83ms
     75%  630.57ms
     90%  795.52ms
     99%    1.14s
  711893 requests in 60.00m, 651.93MB read
  Socket errors: connect 0, read 0, write 0, timeout 419
  Non-2xx or 3xx responses: 6432
Requests/sec:    197.74
Transfer/sec:    185.43KB
```

Current client error rate is around **1%** *(0.9623%)*

![nginx-ingress](https://github.com/1mr/devops-challenge/raw/master/benchmarks/nginx-ingress.png)

![nginx requests](https://github.com/1mr/devops-challenge/raw/master/benchmarks/ngx_requests.png)

![status codes](https://github.com/1mr/devops-challenge/raw/master/benchmarks/ngx_status_code.png)

Tested on:

```bash
# k8s
kubectl version --short
Client Version: v1.19.3
Server Version: v1.18.10

# nginx-ingress
POD_NAMESPACE=ingress-nginx
POD_NAME=$(kubectl get pods -n $POD_NAMESPACE -l app.kubernetes.io/name=ingress-nginx --field-selector=status.phase=Running -o jsonpath='{.items[0].metadata.name}')
kubectl exec -it $POD_NAME -n $POD_NAMESPACE -- /nginx-ingress-controller --version
-------------------------------------------------------------------------------
NGINX Ingress controller
  Release:       v0.34.1
  Build:         v20200715-ingress-nginx-2.11.0-8-gda5fa45e2
  Repository:    https://github.com/kubernetes/ingress-nginx
  nginx version: nginx/1.19.1

-------------------------------------------------------------------------------

# helm
helm version --short
v3.4.0+g7090a89
```
