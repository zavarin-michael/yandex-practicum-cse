#!/bin/bash
set -e

echo "Pushing new version of app to registry"
container_name=$1
image_tag=$2
registry=cr.yandex/crp1m0fdg1u61nn6dc9m/booking:"$image_tag"
docker build -t "$registry" .
docker push "$registry"

echo "Creating new vm with new version"
container_info="$(yc compute instance create-with-container --name "$container_name" --container-image "$registry" --container-env-file '.env' --container-env VERSION="$image_tag",REPLICA_NAME="$container_name" --container-restart-policy 'Always' --platform 'standard-v3' --service-account-id 'aje1cd26sfhfq2kmo7cl' --network-interface subnet-name=default-ru-central1-a,nat-ip-version=ipv4)";
address=$(echo "$container_info" | sed -n 's/.*address: \([0-9\.]*\).*/\1/p' | tail -n 2 | head -n 1);
subnet_id=$(echo "$container_info" | sed -n 's/^.*subnet_id: \([a-zA-Z0-9]*\).*$/\1/p');

echo "Creating new vm with new version"
yc load-balancer target-group add-targets enp4sj58m7uefi63285b --target address="$address",subnet-id="$subnet_id";