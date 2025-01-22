# Valuable Scripts

These scripts can be used as individual components to create applications. They provide basic functionalities and events that help the user utilize the available data and pass it through different channels. These scripts can be found in the `Runtime → Scripts → Interaction Logic` section.

---

## DataStreamingEvents

Events invoked when an exoskeleton connects or loses connection to the SDK respectively.

```csharp
public event Action<HaptikosExoskeleton> OnDataReceived;
public event Action<HaptikosExoskeleton> OnDataStoppedReceiving;
```

---

## ExoskeletonConnectionController

This controller allows you to check the connection status of the exoskeletons.

```csharp
static public bool RightGloveConnected;
static public bool LeftGloveConnected;
```

---

## HaptikosPlayer

The `HaptikosPlayer` class manages calibration states and allows for retrieval of specific exoskeleton scripts based on the hand type.

```csharp
public static bool calibrated; // Boolean that shows whether the exoskeletons should be calibrated

public static HaptikosExoskeleton GetExoskeleton(HandType hand); // Returns the HaptikosExoskeleton scripts of the given hand.
```
These scripts can be found in the `Runtime → Scripts → Interaction Logic`.

---

## InteractionDetector

The `InteractionDetector` script is crucial for managing interactions within Unity environments. It distinguishes between different parts of the hand and manages interactions accordingly, using a dictionary to track multiple simultaneous interactions. This ensures that events are triggered only when the first finger enters or the last finger part exits, which prevents multiple triggers when multiple parts are involved.

This script is ideally suited for GameObjects where functionality needs to be triggered upon touch or removal. It pairs effectively with `HapticFeedback`, as the haptic feedback is triggered when the object is touched.

### Properties and Events

```csharp
public Hand_Part_Type InteractionPart; // Define the selected hand parts.
```

This property allows selection of specific hand parts to trigger interactions. Options include:

  -  `Finger_Tip`
  - `Finger_Middle`
  - `Finger_Base`
  - `Palm`
  - `All`



```csharp
public HandPart LastTouchedFinger;

//Returns the last hand part that touched the object:

public UnityEvent onObjectStoppedTouching;

//Event that triggers when a selected hand part starts touching the object if it was not previously touched.

public UnityEvent onObjectStartTouching;

//Event that triggers when all selected hand parts stop touching the object if it was previously touched.
```

---

## HandPart

Script attached to each part of the model. Contains some information about the hand part.

### Properties

```csharp
public HaptikosExoskeleton ParentHand;
//Reference to the parent `HaptikosExoskeleton` of this hand part. This property acts as a getter and setter.

public Collider Collider;
//Getter/Setter

public List<HandPart> HandPartsInside
//Getter/Setter
//HandParts touching this one.

public Hand_Part_Type Type;
//Getter/Setter
```

---

## HandDetector
This utility script is highly important as it provides information about when an exoskeleton is within an acceptable range and identifies which exoskeleton it is. This functionality is particularly useful for applications that rely on close proximity of the exoskeleton to trigger events. 

The user is able to determine the minimum distance which is then visualized as a green sphere.

```csharp
public HaptikosExoskeleton NearestGlove;
//Get the nearest HaptikosExoskeleton

public bool HandWithinAcceptableDistance;
public List<HandPart> NearestHapticFingers;

public UnityEvent<HaptikosExoskeleton> onHandWithinAcceptableDistance;
//Triggers when an exoskeleton is within the green sphere
	
public UnityEvent<List<HandPart>> onFingerWithinAcceptableDistance;
//Triggers when a specified number of fingers is within the green sphere. Number specified with the serialized field int numberOfFingers;
```

---

## Interaction Delayer

Sometimes when interacting with an object it is necessary to introduce a delay to prevent multiple interactions from being triggered simultaneously. For example, during the development of the switch, an issue arose where the switch could be touched twice in quick succession, causing it to revert to its initial state without notice. This type of issue is common in application development and can be addressed with a simple delay between interactions.
By adding this script to a GameObject, interaction can be temporarily paused. The `StopInteracting` variable can then be used to check whether the object is currently available for interaction.

### Haptikos Gesture Recognizer
This Script is responsible for the gesture recognition process. See the getting started guide here. 
 
#### Properties 

```csharp
public bool poseRecognition;
//If it is false the target handpose is ignored and the result is based solely on the transform Preset 


public bool reversePoseRecognition;
//If true reverses the result of pose Recognition.


public HaptikosHandposeShape targetHandPose;
//A HaptikosHandposeShape, that represents the hand pose to be recognized. 


public bool transformRecognition;
//If it is false the transform preset is ignored and the result is based solely on the target hand pose. 


public bool reverseTransformRecognition;
//If true reverses the result of the transform Recognition.


public HaptikosTransformPreset transformPreset;
//A HaptikosTransformPreset, that describes the accepted directions of the hand. 

public float timeToActivate;
//Defines the time the gesture needs to be continually recognized in order for the activated field to turn true. 
//The value should be larger than 0.01 to avoid flickering of the Activated field. 
//It can also be used with larger values to add a delay to the On Activate event(Hold the gesture for 5 seconds before the event is triggered) 

public float timeToDeactivate;
//Defines the time the gesture needs to be continually not recognized in order for the activated field to turn false. 
//The value should be larger than 0.01 to avoid flickering of the Activated field. 
//It can also be used with larger values to add a delay to the On Deactivate event(trigger the event if the gesture stops being recognized for 5 seconds) 

public bool visualizeTimeToActivate;
//Creates an icon with a green progress to represent the progress towards activation.

public Sprite Icon;
//If Visualize time to Activate or Deactivate is selected, choose the icon to be displayed.
 
public bool Activated;
//True when the gesture is being recognized and false when it is not. 

public UnityEvent<HaptikosExoskeleton> OnActivate;
//Triggers the frame the Activated field turns true


public UnityEvent<HaptikosExoskeleton> OnDeactivate;
//Triggers the frame the Activated field turns false
```

#### Debug Information 

When the project is in play mode every Haptik Gesture Recognizer offers all the relevant information for the Hand Pose Recognition and Transform Recognition through a foldout menu. Keep in mind that when editing a HaptikosHandposeShape or  HaptikosTransformPreset the changes are applied instantly without exiting play mode.

`Current Hand Pose`: Displays all 18 values used to represent the hand pose. 
 
`Show Details`: Shows which of the conditions given by the target hand pose shape are met. 
 
`Transform debug`: all the information about the Transform Recognition 

Especially useful to create and finetune hand pose shapes and transform presets.

---

## HapticFeedback
 
The `HapticFeedback` class is designed to deliver real-time haptic feedback through the exoskeletons, providing an immersive interaction experience. Feedback is dynamically calculated based on interaction states, durations, and specific fingers involved. It uses Unity's AnimationCurve for customizable vibration patterns and supports both continuous and time-limited feedback scenarios.
 
### Features
 
- **Dynamic Feedback**: Adjusts feedback intensity over time using a predefined curve.
- **Multi-Finger Support**: Tracks specific fingers during interactions and sends individual or collective feedback.
- **Hand Differentiation**: Differentiates between left and right hand interactions.
- **Event-Driven**: Integrates UnityEvents for haptic feedback triggers.
 
### Key Properties and Fields
 
```csharp
CustomVibrationCurve curve; 
//Defines the vibration intensity over time.

bool isContinuous;
//Determines if feedback persists or ends after the curve duration.

HashSet<string> activeFingers; 
//Tracks fingers currently involved in the interaction.

HandType activeHandType; 
//Identifies the active hand (left or right).

HaptikosExoskeleton leftGlove, rightGlove; 
//References to the exoskeletons for the left and right hands.

Dictionary<string, string> fingerMappings; 
//Maps finger joints to primary feedback points.
```
 
### Core Methods
 
#### SetCollisionState
 
Sets the collision state for a finger, triggering or stopping feedback.
 
```csharp
bool state; 
//True for active collision, false for inactive.

string finger; 
//Name of the interacting finger.

HandType type; 
//Indicates the hand type (left or right).

bool stopAfterDelay; 
//If true, feedback stops after the curve duration.
```
 
#### SetCollisionStateCoroutine
 
Manages the addition or removal of fingers from the `activeFingers` list. When a finger is added, `isColliding` is set to true if the list count is greater than 0. If `stopAfterDelay` is true, it waits for the curve's duration before removing the finger from the list, stopping the feedback, and resetting the state as needed.
 
Parameters in `SetCollisionStateCoroutine` are same as in `SetCollisionState`.
 
#### RegisterHapticFeedbackListener
 
Registers listeners for haptic feedback start and stop events.
 
#### SendHapticFeedback
 
Sends haptic signals to the specified fingers on the active exoskeleton using a UDP method (`SendHapticData`).
 
```csharp
HashSet<string> fingers; 
//The fingers receiving feedback.

HaptikosExoskeleton exoskeleton; 
//The exoskeleton sending the feedback.

float intensity; 
//Feedback intensity.
```
 
#### StopHapticFeedback
 
Stops haptic signals for the specified fingers using the same UDP method (`SendHapticData`) as before.
 
```csharp
HashSet<string> fingers; 
//The fingers to stop feedback for.

HaptikosExoskeleton exoskeleton; 
//The exoskeleton stopping the feedback.
```
 
#### ResetState
 
Resets all interaction-related states, preparing for new interactions.
 
#### StopAllHaptics
 
Globally stops all haptic feedback with a delay.
 
```csharp
float time;
// Delay before stopping all feedback.
```

---

## HaptikosHandposeShape 

A `ScriptableObject` is used to define and save hand poses. Understanding how to create and finetune hand poses is not required, as a ready to use library is provided.

### HANDPOSE LIBRARY

- **Closed Hand**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Closed_Hand.png" alt="Gestures_Closed_Hand" width="250" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Finger Gun**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Finger_Gun.png" alt="Gestures_Finger_Gun" width="300" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Four**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Finger_Four.png" alt="Gestures_Finger_Four" width="200" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Horns**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Horns.png" alt="Gestures_Horns" width="200" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Index Pinch**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Pinch.png" alt="Gestures_Pinch" width="300" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Index Open Pinch**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Open_Pinch.png" alt="Gestures_Open_Pinch" width="300" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Index Pinch or Open Pinch**

Activates when either pinch or open pinch is detected

- **OK**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_OK.png" alt="Gestures_OK" width="300" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Open Hand**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Open_Hand.png" alt="Gestures_Open_Hand" width="250" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Phone**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Phone.png" alt="Gestures_Phone" width="250" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Point Two Click**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Point_Two_Click.png" alt="Gestures_Point_Two_Click" width="300" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Point Two**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Point_Two.png" alt="Gestures_Point_Two" width="300" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Point One**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Point_One.png" alt="Gestures_Point_One" width="350" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Scissors Three**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Scissors_Three.png" alt="Gestures_Scissors_Three" width="250" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Scissors Two**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gesture_Scissors_Two.png" alt="Gesture_Scissors_Two" width="150" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Stop**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Stop.png" alt="Gestures_Stop" width="250" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Three**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Finger_Three.png" alt="Gestures_Finger_Three" width="200" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- **Thumbs Up**

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Thumbs_Up.png" alt="Gestures_Thumbs_Up" width="300" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

## Customizing Hand Poses in the Library

For those interested in customizing the library or creating new hand poses, understanding the technical details of how hand poses are decoded and defined is crucial.

### Overview of Hand Pose Recognition

The current hand pose is decoded into 18 values, which are used to define what is known as a `Haptik Hand Pose Shape`. A hand pose is recognized if the current hand pose's measurements fall within the acceptable ranges for all 18 values.

### Pose Value Composition

Each finger's movement is quantified by four values: curl, flexion, abduction, and opposition, with the following specifics:

- `Thumb Opposition` and `Pinky Abduction` are not included in these measurements, which leaves a total of 18 values.
  
#### Specific Metrics for Fingers (Except the Thumb)

- `Curl`: This is measured as the angle of the last two joints divided by two. 
  - `Expected range`: -20 to 105 degrees.

- `Flexion`: This is the angle of the joint at the base of the finger.
  - `Expected range`: -30 to 85 degrees.

The calculation for these angles is depicted in Figure 1:
- `Curl` is calculated as \(φ1 + φ2\)
- `Flexion` is represented as \(θ\)

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Angles_Curl_Flexion.png" alt="Gestures_Angles_Curl_Flexion" width="400" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

This detailed description enables users to accurately set parameters for new hand poses based on precise angle measurements and ranges.

#### Abduction and Opposition for Fingers

- `Abduction`: The angle between this finger and the next finger, starting from the thumb.
  - `Expected range`: -10 to 25 degrees.
  - As shown in Figure below, abduction is represented as \(θ\).

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Angles_Abduction.png" alt="Gestures_Thumbs_Up" width="200" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- `Opposition`: The distance in centimeters between the tip of the finger and the thumb tip.
  - `Expected range`: 0 to 25 cm.


<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Angles_Opposition.png" alt="Gestures_Thumbs_Up" width="400" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

### Specific Metrics for the Thumb

The thumb has unique metrics compared to other fingers, defined as follows:

- `Curl`: The angle of the last joint of the thumb.
  - `Expected range`: -25 to 105 degrees.

- `Abduction`: The angle of the plane perpendicular to the picture from the axis of the index when it is straight to the base joint of the thumb.
  - `Expected range`: -10 to 45 degrees.
  - As shown in Figure below, curl = \(θ\) and flexion = \(φ\).

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Gestures_Angles_Curl_Abduction.png" alt="Gestures_Angles_Curl_Abduction" width="400" />
  <p style="font-size: 14px; color: gray;"></p>
</div>

- `Flexion`: The angle of the plane perpendicular to the picture from the axis of the index when it is straight to the base joint of the thumb.
  - `Expected range`: -30 to 55 degrees.
  - We define the value of flexion positive when the thumb is outwards, as shown in Figure below.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px; display: flex; justify-content: center; gap: 20px;">
  <div>
    <img src="_static/Gestures_Angles_Positive_Abduction.png" alt="Gestures_Angles_Positive_Abduction" width="400" />
  </div>
  <div>
    <img src="_static/Gestures_Angles_Negative_Abduction.png" alt="Gestures_Angles_Negative_Abduction" width="356" />
  </div>
</div>


### Configuring HaptikosHandposeShape

Once the desired values are determined, they can be input into a `HaptikosHandposeShape` through the custom inspector. The input values represent the minimum and maximum accepted ranges. Certain values can be ignored if they are not necessary to define.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px; display: flex; justify-content: center; gap: 20px;">
  <div>
    <img src="_static/Gestures_Editor_Edit_Mode.png" alt="Gestures_Editor_Edit_Mode" width="250" />
  </div>
  <div>
    <img src="_static/Gestures_Editor_Display_Mode.png" alt="Gestures_Editor_Display_Mode" width="250" />
  </div>
</div>