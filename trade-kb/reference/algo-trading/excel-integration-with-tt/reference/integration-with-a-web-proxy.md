---
title: Integration with a web proxy
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/reference/integration-with-a-web-proxy/
---

# Integration with a web proxy

> Category: **Algo Trading** · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/reference/integration-with-a-web-proxy/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § Excel / RTD linking](../../../../guides/algo-ops.md#excel-rtd-linking)

To use Excel integration in TT, the client workstation requires DNS access to localhost-tradingtechnologies.com on port 8181. If your corporate network uses a web proxy, you will need to make some additional configuration changes to ensure that communiation between TT or TT Desktop and the Excel COM add-in functions properly.

When using the Excel add-in to communicate with TT, a secure websocket application is launched local on the workstation that uses TLS certificates for a secure websocket. The TCP/IP communication runs via the workstation’s loopback ip address of 127.0.0.1. The **localhost-tradingtechnologies.com** URL resolves to **127.0.0.1**. TT Manages the TLS certificate however it is client’s responsibility to ensure this traffic stays local to the workstation so it is required that **localhost-tradingtechnologies.com** be excluded from web proxies.

## Verifying the Excel add-in is enabled

By default, the Excel add-in is automatically enabled during installation. If, for some reason, the add-in is later disabled, the TT platform will be unable to communicate with Excel.

To verify or re-enable the Excel add-in:

1. Start the Excel application, if necessary.
2. From the **File** menu, select **Options**; then click **Add-ins** in the **Excel Options** dialog.You shoud see **TT Excel Integraion** in the list of **Add-ins**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-excel-add-in.png)
3. From the **Manage** dropdown, select **COM Add-ins** and click **GO**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-excel-com-add-in.png)
4. Verify, or enable, **TT Excel Integration** and click **OK**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-excel-enable-add-in.png)

## Bypassing the web proxy for localhost-tradingtechnologies.com

To verify that the loopback address resolves to 127.0.0.1 and is connecting through port 8181, enter the following commands is a Windows Command Prompt window:

* ping localhost-tradingtechnologies.com
* netstat -n | findstr 8181

You should see multiple instances of 127.0.0.1:8181 request/response pairs.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-web-proxy-bypass-shell.png)

To add localhost-tradingtechnologies.com to the web proxy bypass:

1. From the **Control Panel**, open the **Internet Properties** and select the **Connections** tab.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-web-proxy-internet-properties.png)
2. Click **LAN settings**; then enable **Use a proxy server for your LAN**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-web-proxy-lan-settings.png)
3. Click **Advanced**; then add **localhost-tradingtechnologies.com** to the **Exceptions** and click **OK**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-web-proxy-bypass-exceptions.png)

**Note**: If, in your troubleshooting, you happen to see traffic on TCP Port 8181 on your web-proxy via **tcpdump** (packet capture); you will have not yet successfully implemented the web-proxy bypass. Please re-check your .pac file to be sure the “localhost-tradingtechnologies.com” web-proxy bypass statement is correctly added and loaded on the trader workstation.

[Next PostExcel integration troubleshooting](excel-integration-troubleshooting.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-excel-add-in.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-excel-com-add-in.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-excel-enable-add-in.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-web-proxy-bypass-shell.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-web-proxy-internet-properties.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-web-proxy-lan-settings.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-web-proxy-bypass-exceptions.png
