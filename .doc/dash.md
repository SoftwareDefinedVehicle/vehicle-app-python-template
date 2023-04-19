### Precondition



### Dash Command

```java
java -jar org.eclipse.dash.licenses-0.0.1-20230403.055043-775.jar clearlydefined.input -review -token <token> -project automotive.velocitas -summary DEPENDENCIES
```

With proxy:
```java
java \
    -Dhttp.proxyHost=host.docker.internal \
    -Dhttp.proxyPort=3129 \
    -Dhttps.proxyHost=host.docker.internal \
    -Dhttps.proxyPort=3129 \
    -Dhttp.nonProxyHosts="localhost|127.0.0.1|host.docker.internal" \
    -Dhttps.nonProxyHosts="localhost|127.0.0.1|host.docker.internal" \
    -DsocksProxyHost=host.docker.internal \
    -DsocksProxyPort=3129 \
    -jar org.eclipse.dash.licenses-0.0.1-20230403.055043-775.jar \
    clearlydefined.input \
    -review \
    -token <token> \
    -project automotive.velocitas \
    -summary DEPENDENCIES
```
