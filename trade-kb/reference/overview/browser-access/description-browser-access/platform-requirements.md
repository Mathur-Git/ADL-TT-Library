---
title: Platform requirements
category: Overview
source: https://library.tradingtechnologies.com/trade/overview/browser-access/description-browser-access/platform-requirements/
---

# Platform requirements

> Category: **Overview** · [Source](https://library.tradingtechnologies.com/trade/overview/browser-access/description-browser-access/platform-requirements/)
>
> **Interpreted in:** [Platform & Workspace § TT Desktop vs browser access vs mobile](../../../../guides/platform-and-workspace.md#tt-desktop-vs-browser-access-vs-mobile)

Before accessing the TT platform, ensure that you meet the TT [system](#system),
[network](#network), and [email](#email) requirements.

## System Requirements

To ensure the best experience, TT recommends the following setup on any machine or mobile device that you use to access the TT platform.

### Browser Requirements

TT supports the latest two versions of the following browsers:

* Google Chrome
* Firefox
* Microsoft Edge**Note**: As Microsoft has discontinued support for Internet Explorer, TT no longer supports Internet Explorer.

Users should verify that the browser is set to automatically update.

**Note:** Users should also verify that cookies are accepted in their browser.

### Hardware Requirements

TT recommends a minimum of 4GB of RAM on any machine or mobile device that you use to access the TT platform. For mobile access, ensure that you have enough storage on your device to store the TT Mobile application. Access to the TT platform is independent of the type of hardware (e.g., laptop, mobile) or operating system (e.g., Mac OS, Windows, iOS, Android) that you use.

### Mobile Requirements

Trading Technologies recommends the following minimum operating system versions for use with the TT Mobile application:

* iOS 8
* Android KitKat (4.4)

## Network Requirements

Client workstations must support https traffic (via Transport Layer Security) over port **443** to/from the TT Platform. Therefore, the firm’s administrator must allow traffic to the TT Platform’s domain as opposed to a specific range of IP addresses. This can be accomplished by either updating firewall restrictions or using an https web proxy.

You can verify connectivity by pointing a web browser on the client workstation to the following location:

<https://trade.tt>

### Requirements for Excel Integrations

Please ensure that your workstation host clock is syncing from a reliable time source. If the system is clock is off by more than a minute, the Excel integration will fail to connect.

In addition to the network requirements above, in order to use [TT’s Excel integration](../../../algo-trading/excel-integration-with-tt/description-excel-integration-with-tt/excel-integration-with-tt-overview.md) the client workstation requires DNS access to **localhost-tradingtechnologies.com** on port **8181**.

**Note**: If your enterprise network implements a web proxy, you need to perform additional steps to support Excel intergration. For more information, see [Integration with a web proxy](../../../algo-trading/excel-integration-with-tt/reference/integration-with-a-web-proxy.md).

## Email Requirements

Trading Technologies uses email to send a number of communications including users’ initial invitations and notices for general system maintenance. To ensure receipt of invitations, notices, and advisories, users must ensure they can receive emails from **TT’s sender address**.

Users should add **TT’s sender address** as a contact in their mail client. In addition, company administrators should configure **TT’s sender address** as a valid address for their company email.

←[Previous PostBrowser Access Overview](browser-access-overview.md)

[Next PostHome Page](home-page.md)→

