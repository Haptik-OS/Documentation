# Haptikos Core Application

## Setting Up the Application

1. **Extract the Files**  
   First, extract (unrar) the contents of the `.rar` file provided.  
   Double-click on `Haptikos Official App.exe` to run the application.  

2. **Importing the License**  
   When you first open the application, you must import the license that comes with the set of exoskeletons.  
   - On the **Haptikos Official App**, click on the `Upload License Icon` located at the top right.  
   - The license is included with the pair of exoskeletons you received, in the `.json` format.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/uploadlicense.png" alt="uploadlicense" width="600" />
  <p style="font-size: 14px; color: gray;">Figure 1: Uploading a License</p>
</div>

---

## Creating a Project

1. **Create a New Project**  
   - Click the `Create New Project` button.  
   - In the dialog that appears, tap `Create`.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px; display: flex; justify-content: center; gap: 20px;">
  <div>
    <img src="_static/createproject1.png" alt="createproject1" width="400" />
  </div>
  <div>
    <img src="_static/createproject2.png" alt="createproject2" width="400" />
  </div>
</div>
<p style="font-size: 14px; color: gray; text-align: center;">Figure 2: Create a Project</p>

---

## Creating a Profile

1. **Setting Up a Profile**  
   - A `Profile` holds user data such as `Finger Length Data` and `Hand Direction`.  
   - After creating a `Project`, you will be prompted to create a `Profile` on the next screen.  

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px; display: flex; justify-content: center; gap: 20px;">
  <div>
    <img src="_static/createprofile1.png" alt="createprofile1" width="400" />
  </div>
  <div>
    <img src="_static/createprofile3.png" alt="createprofile3" width="400" />
  </div>
</div>
<p style="font-size: 14px; color: gray; text-align: center;">Figure 3: Create first profile</p>

   - The `Profile` can be also  be created by pressing the `Circular Button` (Figure 4).

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
<img src="_static/createprofile2.png" alt="createprofile2" width="600" />
<p style="font-size: 14px; color: gray;">Figure 4: Create a profile
</p>
</div>

---

## Calibration Procedure

The calibration procedure consists of two steps:  

### 1. Finger Calibration  
   - Wear the **Right Exoskeleton** on your hand as shown in Figure 5.  
   - Press the `Spacebar` to acquire finger tracking data.  

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
<img src="_static/calibration.png" alt="calibration" width="600" />
<p style="font-size: 14px; color: gray;">Figure 5: Finger Calibration
</p>
</div>

### 2. Hand Direction Calibration  
   - Face the direction of the screen.  
   - Press `R` to calibrate the hand direction.  
   - This ensures the hand direction in the application matches the direction the headset is looking.  

> **Important Notice:**  
> Calibration can also be performed through the SDK. Use the **Haptikos Core Application** for testing and development purposes.

### Connection Reminder  
If the right exoskeleton is not connected during calibration, a warning screen will appear, signaling that the exoskeleton must be connected.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
<img src="_static/calibrationwarning.png" alt="calibrationwarning" width="600" />
<p style="font-size: 14px; color: gray;">Figure 6: Calibration Warning Screen
</p>
</div>

---

## 3D View of Hands

Once calibration is completed:  
- A 3D view of the hands will be displayed.  
- The right-hand data is connected and ready to stream to the **Unity Application**.  

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
<img src="_static/sceenview.png" alt="calibrationsceenviewwarning" width="600" />
<p style="font-size: 14px; color: gray;">Figure 7: 3D Scene View
</p>
</div>

In the top right corner, you can view:  
- Connected exoskeletons.  
- Battery levels.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
<img src="_static/contents.png" alt="contents" width="600" />
<p style="font-size: 14px; color: gray;">Figure 8: 3D Contents
</p>
</div>

---

## Profiles Section

- You can create a `New Profile` by clicking the `Circular (+) Button` from the main menu.  

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
<img src="_static/createprofilemenu.png" alt="createprofilemenu" width="600" />
<p style="font-size: 14px; color: gray;">Figure 9: Creating Profile 3D Menu Screen
</p>
</div>

- Restart the `Hand Direction Calibration` and `Fingers Calibration` using the buttons provided.  

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px; display: flex; justify-content: center; gap: 20px;">
  <div>
    <img src="_static/recalibration1.png" alt="recalibration1" width="400" />
  </div>
  <div>
    <img src="_static/recalibration2.png" alt="recalibration2" width="400" />
  </div>
</div>
<p style="font-size: 14px; color: gray; text-align: center;">Figure 10: Recalibration Process</p>

> **Note:** At least the right glove needs to be connected for calibration.

---

## Recordings

1. Creating Recordings  
   - Connect at least one exoskeleton.  
   - Press the `White Circle` to prompt the recording dialog and `Create a recording`.  

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px; display: flex; justify-content: center; gap: 20px;">
  <div>
    <img src="_static/createrec1.png" alt="createrec1" width="400" />
  </div>
  <div>
    <img src="_static/createrec2.png" alt="createrec2" width="400" />
  </div>
</div>
<p style="font-size: 14px; color: gray; text-align: center;">Figure 11: Creating a recording</p>

2. Stopping Recordings  
   - Press the `Stop` button.  
   - The recording will appear in the `Recordings List` at the top left.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px; display: flex; justify-content: center; gap: 20px;">
  <div>
    <img src="_static/recsave1.png" alt="recsave1" width="400" />
  </div>
  <div>
    <img src="_static/recsave1.png" alt="recsave2" width="400" />
  </div>
</div>
<p style="font-size: 14px; color: gray; text-align: center;">Figure 12: Recordings Save</p>

3. Accessing Recordings 
   - Press the `Folder Icon` to open the `Recordings` folder.  
   - Each `Profile` has different `Recordings` for each `Project`.  

4. Playback Options  
   - Use the `Play Button` to view `Recordings`.  
   - Press the `X Button` to delete `Recordings`.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px; display: flex; justify-content: center; gap: 20px;">
  <div>
    <img src="_static/playdelrec1.png" alt="playdelrec1" width="400" />
  </div>
  <div>
    <img src="_static/playdelrec2.png" alt="playdelrec2" width="400" />
  </div>
</div>
<p style="font-size: 14px; color: gray; text-align: center;">Figure 13: Play & Delete Recordings</p>


---

## Playback Recordings in Unity

1. Export and Move Recordings  
   - Locate `Recordings` by clicking the `Folder Icon`.  
   - Move the `Recording` into a `Unity` project containing the **Haptik_OS SDK**.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
<img src="_static/foldericon.png" alt="foldericon" width="600" />
<p style="font-size: 14px; color: gray;">Figure 14: Folder Icon
</p>
</div>

2. Playback Setup  
   - Navigate to `Haptikos → Built-in Scene Loader`.  

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
<img src="_static/Haptikos_Panel2.png" alt="Haptikos_Panel2" width="150" />
<p style="font-size: 14px; color: gray;">Figure 15: Haptikos Panel
</p>
</div>

   - Select `Recording Playback` to load the scene.  

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
<img src="_static/selrec.png" alt="selrec" width="150" />
<p style="font-size: 14px; color: gray;">Figure 16: Selecting Recording Playback scene
</p>
</div>

3. Using the `Playback Hand`  

   In the scene, the `Playback Hand` can be found. This prefab is used to playback the recordings that are captured from the **Haptikos Core Application**. This prefab can also be found in the `Haptikos Panel`, under `Player`. This panel in the SDK is mostly used to spawn the most important elements in the scene, without having to navigate through the SDK. It is recommended that it is used for convenience.

### Recording Playback Options  

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
<img src="_static/recoptions.png" alt="recoptions" width="700" />
<p style="font-size: 14px; color: gray;">Figure 17: Recording playback options
</p>
</div>

- **Recording Placement**: Choose where the recording is placed.  
- **Playback Bar**: Manipulate the recording in `Edit Mode`.  
- **Sample Rate**: Lower sample rate means higher playback speed.  
- **Recording Hand**: Playback can be adjusted to the left or right hand, and changed during runtime.