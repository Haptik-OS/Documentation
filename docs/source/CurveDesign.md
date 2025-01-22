# Haptics

This document provides a step-by-step guide for configuring and using the `Custom Vibration Curve` system for the **Haptikos Exoskeleton**. Below, each component and operation are explained in detail to ensure smooth integration and usability.

---

## Creating a Custom Vibration Curve

1. Navigate to `Assets -> Create -> ScriptableObjects -> CustomVibrationCurve`.
2. Provide a name for the new vibration curve and select it.

---

## Components of the Custom Vibration Curve

### Curve Display
- **Description:** A visual representation of the vibration curve. This allows the user to see the current configuration of the curve.

### Curve Operations
- **Restart Curve:** Resets the curve to its default state, which is an empty curve.

### Pattern Operations

#### Pattern Generation
Generate predefined patterns such as:
- `Linear Curve`
- `Inverse Linear Curve`
- `Sinusoidal Curve`
- `Exponential Curve`
- `Inverse Exponential Curve`

#### Pattern Modification
Modify the basic values of the generated patterns:
- **Start Curve Value:** Defines the starting amplitude of the curve. For a sine wave, this represents the minimum amplitude.
- **End Curve Value:** Defines the end amplitude of the curve. For a sine wave, this represents the maximum amplitude.
- **Curve Duration:** Sets the length of time for the curve.

---

## Audio-to-Curve Operations

This feature converts an audio clip into a vibration curve.

### Components

- **Audio Clip:** Add an audio clip to transform it into a vibration curve.
- **Original WAV:** A visualization of the uploaded audio clip.
- **Sample Count:** Defines the resolution of visualization (default is 1024; higher values yield better resolution).
- **Convert Audio to Curve:** Press this button to generate the vibration curve visualization from the audio clip.

### Edited WAV File

**Description:** A modified version of the original WAV file using specific settings.

#### Settings:
- **Minimum Amplitude:** Sets the minimum value for the edited WAV file.
- **Maximum Amplitude:** Sets the maximum value for the edited WAV file.
- **Keyframe Time Interval:** Defines the time between each keyframe.
- **Start Time and Duration:** Select the start and end times of the audio clip for editing.

**Apply Changes:** Press the `Apply Curve Edits` button to finalize the modifications. For example, if the original clip is 50 seconds long and only 1 second is needed, it can be trimmed to the desired length.

### Peaks WAV File

**Description:** Displays only the prominent peaks of the WAV file for further refinement.

**Apply Changes:** Press `Apply Only Peaks` to finalize the peaks-focused visualization.

---

## Advanced Curve Operations

### Keyframe Editing

Add, modify, or delete keyframes:

- **Edit Keyframes:** Change the time, value, in-tangent, or out-tangent values.
- **Remove Specific Keyframe:** Deletes a selected keyframe.
- **Remove All Keyframes:** Clears all keyframes from the curve.
- **Add New Keyframe:** Set the time, value, in-tangent, and out-tangent, then press `Add Keyframe`.

### Curve Duration Modification

Adjust the overall duration of the curve:
- For example, transform a 1-second clip into a 3-second curve by specifying the new duration and pressing `Apply Curve Duration Scaling`.
- Reset the curve to its original duration if needed by pressing `Reset Curve Duration Scaling`.

---

## Curve Data Visualization

- Open the `HapticsVisualization` scene.
- Navigate to the `Vibration Curve Visualizer` gameobject.
- Assign the created vibration curve to the `Curve Data` field in the `Curve Cursor Visualizer` script located within the GameObject.
- Turn on `Gizmos` to see the visualization of the curve.
- Choose the hand for experiencing the curve from the dropdown menu.

### Additional Buttons for Control:
- **Start:** Starts a single wave of the curve.
- **Pause:** Temporarily halts the curve.
- **Reset:** Resets the vibration to the start of the curve.
- **Toggle Loop:** Continuously loops the vibration curve until it is stopped by the user by pressing it again.

---
