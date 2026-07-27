---
title: User Acceptance Testing (UAT) Environment
category: Overview
source: https://library.tradingtechnologies.com/trade/overview/tt-platform/description-tt-platform/user-acceptance-testing-uat-environment/
---

# User Acceptance Testing (UAT) Environment

> Category: **Overview** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/overview/tt-platform/description-tt-platform/user-acceptance-testing-uat-environment/)

Prior to releasing new functionality to the Production environment, TT® provides a
separate User Acceptance Testing (UAT) Certification environment at [uat.trade.tt](https://uat.trade.tt/). The TT UAT environment connects to actual exchange certification environments for both market data and order routing.

When enabled, users may access the environment via the browser application, TT Desktop, and/or our APIs.

## Accessing the UAT Certifcation Environment

### Administrator Access to the UAT Environment in Setup

To test new functionality, adminstrators may connect to [Setup](https://setup-uat.trade.tt/ext-uat-cert) in the UAT environment.

### Enabling User Access to the UAT Environment in Setup

Adminstrators may assign access to the UAT environment to individual traders and developers using the **Environments** tab under **Users** in Setup.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/uat-add-user.png)

For more information on settting up users, refer to the [Managing Environments for a User](https://library.tradingtechnologies.com/user-setup/us-managing-users.html#env) section in the Setup Help.

### Accessing via TT Application Programming Interface

Developers may connect to the UAT environment using one of the following TT APIs:

* **TT REST API**: allows you to integrate your applications using the same REST services used by TT.
* **TT .NET SDK**: build your own client or server-side Windows applications.
* **TT CORE SDK**: build your own server-side Linux applications.

In addition to gaining trading access to the UAT environment, developers must also create and manage application keys in order to run their custom trading applications. The same order permissions and account restrictions assigned to you as a user in Setup also apply to you when you log in and trade via your key-based trading application.
Whether you log in via a browser or key-based trading application, your same user order permissions and account restrictions apply in both cases.

For more information on application keys, refer to the [Creating and Managing Application Keys](https://library.tradingtechnologies.com/user-setup/us-creating-and-managing-application-keys.html) section in the Setup help.

### Accessing via TT FIX

Prior to accessing the UAT environment, TT FIX applcations must first complete TT’s FIX Certification. This process includes configuring connectivity to the environment, setting up FIX sessions in Setup, and working with the FIX Integration team to certify and review your application.

For a complete description of the TT FIX Certification process, refer to [TT FIX Certification](https://library.tradingtechnologies.com/tt-fix/general/Certification.html) section in the TT FIX help.

## Workspaces in the UAT trading environment

You can log into [uat.trade.tt](https://uat.trade.tt/) using your existing TTID credentials.

When you log into the UAT environment, your workspaces from the Live and Simulation environments will not be
available to use. Conversely, workspaces that you create for UAT trading will not be available for use in the Live and Simulation environments.

To use your Live or Simulation environment workspaces for UAT trading, you can export the workspace from Live/Simulation then import it into uat.trade.tt using the [workspace importing and exporting functionality](../../tt-desktop/task-tt-desktop/importing-and-exporting-workspaces.md) available in TT.

**Note**: If you import a workspace, any widgets or features in the workspace that are unsupported in that particular environment will be filtered out when you open the workspace.

## Using the UAT Certification Trading Environment

After you open your workpsace, you’ll notice each open widget in the workspace includes a **Certifcation Session** banner.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/uat-banner.png)

## TT Support Center

The [TT® Support Center](https://www.tradingtechnologies.com/resources/tt-support-center/) can help answer additional questions on UAT access and configuration. TT Support contact information is as follows:

* Americas: +1 312 476 1002
* Asia / Pacific: +65 6395 7002
* Australia: +61 2 8022 1702
* Europe / Middle East: +44 20 7621 8181
* Japan: +81 3 4577 8302

←[Previous PostMock Trading Support](mock-trading-support.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/uat-add-user.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/uat-banner.png
