function FindProxyForURL(url, host) {
    // Check for exempted domains
    // Check for exempted IP address
    var exemptedIP = "34.87.112.9"; // Ganti dengan IP yang ingin dikecualikan
    if (isInNet(host, exemptedIP, "255.255.255.255")) {
        return "DIRECT";
    }

    // Default proxy for all other URLs
    return "PROXY turbo-r7k1ssza.edge.prod.fortisase.com:9443; DIRECT";
}