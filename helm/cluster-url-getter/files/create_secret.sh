CONSOLE_URL=$(oc get route console -n openshift-console -o go-template='{{if .spec.tls}}https://{{else}}http://{{end}}{{.spec.host}}{{"\n"}}')
BASE_URL=.apps$(echo $CONSOLE_URL | sed 's/^.*apps//g')
if oc get secret cluster-url >/dev/null 2>&1; then
  oc delete secret cluster-url
fi
oc create secret generic cluster-url --from-literal=BASE_URL="$BASE_URL"