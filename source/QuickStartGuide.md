# Quick Start Guide

The first step is to put on the **Haptikos Exoskeleton**, as shown in Figure 1.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
<img src="_static/wearcorrect.png" alt="wearcorrect" width="300" />
<p style="font-size: 14px; color: gray;">Figure 1: User wearing the exoskeletons correctly
</p>
</div>

Wearing the exoskeleton as closely as depicted in Figure 1 will result in improved calibration and greater finger and hand accuracy. After putting on the exoskeletons, ensure that the dongle is connected to the PC and activate the exoskeletons by pressing the corresponding button. Once the exoskeletons are successfully turned on, a green light will appear, indicating that the device is active and connected.

> **Note:** The dongle's green light turns on even if only one exoskeleton is connected.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px; display: flex; justify-content: center; gap: 20px;">
  <div>
    <img src="_static/greendon.png" alt="greendon" width="400" />
  </div>
  <div>
    <img src="_static/whitedon.png" alt="whitedon" width="224" />
  </div>
</div>
<p style="font-size: 14px; color: gray; text-align: center;">Figure 2: Green light on the dongle and white light on the exoskeleton</p>

## Connecting to the Haptikos Core Application

After opening and connecting both exoskeletons, the **Haptikos Core Application** should be launched. This application acts as a bridge between the exoskeletons and the PC, enabling data streaming from the exoskeletons to Unity. It also provides user profiling by recording hand length and calibration data to ensure the exoskeletons are adjusted correctly.

The download link for the **Haptikos Core Application** is the following: *(Insert download link)*.

### License Import

Once downloaded, proceed to import the `License`, a `.json` file uniquely provided for each pair of exoskeletons. The **Haptikos Core Application** will first prompt for `License` import.

### Creating Projects and Profiles

After the `License` is imported:

1. Create a `Project`.
2. Create a `Profile`.

For more information about profiles, projects, and the **Haptikos Core Application**, refer to the related section.

## Streaming Data to Unity

After completing the setup and exoskeletons’ calibration, the data can be streamed into Unity.

---