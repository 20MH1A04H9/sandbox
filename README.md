
# Windows Sandbox

Windows Sandbox provides a lightweight desktop environment to safely run applications in isolation. Software installed inside the Windows Sandbox environment remains "sandboxed" and runs separately from the host machine.



## The Requirements

- ARM64 (for Windows 11, version 22H2 and later) or AMD64 architecture, with a virtual machine enabled in the BIOS.
- At least 4 GB of RAM (8 GB is recommended).
- At least 1 GB of free disk space (SSD is used).
- At least two CPU cores (four cores with hyperthreading are mentioned).

## Installation

First that your machine is using Windows 10 Pro or Enterprise, build version 18305 or Windows 11.

Enable virtualization on the machine.

PowerShell commands
```bash
  Set-VMProcessor -VMName <VMName> -ExposeVirtualizationExtensions $true
  Update-VMVersion -VMName <VMName>
```
    
    
Use the search bar on the task bar and type Turn Windows Features on or off to access the Windows Optional Features tool. Select Windows Sandbox and then OK. Restart the computer


Open PowerShell as Administrator:

```bash
  Enable-WindowsOptionalFeature -FeatureName "Containers-DisposableClientVM" -All -Online
```
## License

[Windows SandBox License](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file#networking)

[Windows Sandbox configuration](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file)

[Diagnostic Data Viewer](https://learn.microsoft.com/en-us/windows/privacy/diagnostic-data-viewer-overview)
