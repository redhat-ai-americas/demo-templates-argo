# Cluster URL Getter

Spins up a job that gets the base apps URL of the cluster and saves it off to a secret. This is often required for other elements of this repository to work, so I recommend running it first in a new cluster. That said, don't rely on the service account and authorization to do work, since the secret can also be created manually.