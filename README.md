# Keylogger
Software that keeps track of and records your keystrokes as you type.

**Note:** The installation description is for a specific case to make it easier to understand how it works.

## What It Consists Of
The package consists of three programs – svchost.py (the main program that records data), MicrosoftStoreUpdate.py (the program that adds itself to autostart), and MinecraftSetup.py (an auxiliary program used to download the previous two).

## What It Does
The program logs keystrokes and reads system information, then, at a set interval (default: 60 seconds), sends the collected information via email.

## Delivery Method
The condition for successful execution is the assumption that the recipient of the message is a user with administrator privileges. Additionally, the user must belong to the group of naive users – when the PowerShell confirmation window appears, they should assume it is just a normal installation process.

The initial stage involves gathering information about the victim using open-source intelligence (OSINT). We obtain information about their email address. Later, we discover that it is linked to their social media accounts. From the analysis, it turns out that the target is a fan of the game Minecraft. This action aims to personalize the phishing email to better fit the victim.

The next step is sending an email encouraging the target to download the application. The victim receives an email with a link to download the beta version of the newest Minecraft release and become a tester.

## Installation On The Victim’s Computer
The victim must download the MinecraftSetup.exe file and then run it. The remaining programs will be downloaded and executed automatically, and afterwards moved to the folder:
```
C:\Users\Public\Pobierane pliki prywatne
```
with the hidden attribute enabled.

## Mechanisms For Delivering Information To The Attacker

The first step is to create an account on https://mailtrap.io and change the values of EMAIL_ADDRESS and EMAIL_PASSWORD in the svchost.py file to your own.

Next, a repository needs to be created on GitLab (or another service) and the compiled executables svchost.exe, MicrosoftStoreUpdate.exe, and the installer for Minecraft should be uploaded there.

In the following step, the MinecraftSetup.py file must be edited to include the correct GitLab (or other service) links.

The last step is to upload the compiled executable MinecraftSetup.exe to any file-hosting service.

## Handling The Received Information
The information will be delivered by email, so the attacker simply needs to read the received messages.

**Note:** This code DOES NOT promote or encourage any illegal activities! The content in this document is provided solely for educational purposes and to create awareness!
