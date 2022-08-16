#!/bin/bash
export HOME="/dapr"
./dapr run \
--app-id $DAPR_APP_ID \
--app-port $DAPR_GRPC_PORT \
--dapr-grpc-port $DAPR_GRPC_PORT \
--dapr-http-port $DAPR_HTTP_PORT \
--config ./.dapr/config.yaml \
--components-path ./.dapr/components \
./run-exe