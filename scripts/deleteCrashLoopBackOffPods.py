#!/usr/bin/env python

from kubernetes import client, config
import argparse
from os import path


def killPods(ns='default'):
    """

    :type ns: str
    """
    v1 = client.CoreV1Api()
    print("Check CrashLoopBackOff Pods:")
    ret = v1.list_namespaced_pod(namespace=ns)

    for i in ret.items:
        if i.metadata.owner_references[0].kind != "Job":
            status = i.status.container_statuses[0]
            if (status.ready is False) and (status.started is False):
                name = i.metadata.name
                restart = status.restart_count
                if restart > 3:
                    reason = status.state.waiting.reason
                    if reason == 'CrashLoopBackOff':
                        msg = status.state.waiting.message
                        print("Deleting pod...")
                        print("%s\t%s\t%s\t%s" % (name, reason, restart, msg))
                        v1.delete_namespaced_pod(namespace=ns, name=name)


if path.exists('/run/secrets/kubernetes.io/serviceaccount/namespace'):
    config.load_incluster_config()
    with open('/run/secrets/kubernetes.io/serviceaccount/namespace', 'r') as ns:
        namespace = ns.read().strip()
    killPods(namespace)
else:
    config.load_kube_config()
    parser = argparse.ArgumentParser()
    parser.add_argument("-ns", "--namespace", help="namespace name")
    args = parser.parse_args()
    killPods(args.namespace)
