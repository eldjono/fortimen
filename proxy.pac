function FindProxyForURL(url, host) {
    if (shExpMatch(url, "https://34.87.112.9:14000/saml*")) {
        return "DIRECT";
    }
    return "PROXY turbo-r7k1ssza.edge.prod.fortisase.com:9443; DIRECT";
}
