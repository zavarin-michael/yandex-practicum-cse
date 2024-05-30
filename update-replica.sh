#!/bin/bash
set -e

echo "Pushing new version of app to registry"
container_name=$1
image_tag=$2
registry=cr.yandex/crp1m0fdg1u61nn6dc9m/booking:"$image_tag"
docker build -t "$registry" .
docker push "$registry"

echo "Updating new vm with new version"
yc compute instance update-container "$container_name" --container-image "$registry" --container-env-file '.env' --container-env VERSION="$image_tag",REPLICA_NAME="$container_name" --container-restart-policy 'Always';
