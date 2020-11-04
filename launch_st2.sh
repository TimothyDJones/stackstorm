#!/usr/bin/env sh
export ST2_VERSION=3.2.0
export ST2_EXPOSE_HTTP=127.0.0.1:8080
docker-compose up -d
docker-compose exec st2client bash
