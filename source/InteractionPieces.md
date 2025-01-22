# Interactable Objects

The SDK contains premade interaction pieces, with haptic feedback, that can be used directly to create simple yet effective everyday interactions. These include: 

- `Haptikos Table Button`
- `Haptikos Dimmer`
- `Haptikos Table Switch`
- `Haptikos Wall Switch`
- `Haptikos Lever`
- `Haptikos Slider`
- `Haptikos Grabbable Object`

## Haptikos Table Button

This is the simplest of all interactions: a table button that can be pressed using a hand.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Table_Button.png" alt="Table_Button" width="400" />
  <p style="font-size: 14px; color: gray;">Figure 1: Haptikos Table Button</p>
</div>

The button consists of multiple scripts that execute parts of the logic. These scripts are easily configurable and ready to use in other interactables. Their simplicity facilitates the creation of interactions with ease.

### Haptikos Table Button Hierarchy and Scripts

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Table_Button_Hierarchy.png" alt="Haptikos_Table_Button_Hierarchy" width="300" />
  <p style="font-size: 14px; color: gray;">Figure 2: Haptikos Table Button Hierarchy</p>
</div>

The scripts that the `Haptikos_Table_Button` contains are:

- `Haptikos Button`
- `Haptic Feedback`
- `Rigidbody Locker`

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Pressable_Button_GO_Scripts.png" alt="Haptikos_Table_Button_Scripts" width="500" />
  <p style="font-size: 14px; color: gray;">Figure 3: Haptikos Table Button Scripts</p>
</div>

The `Haptikos Button` script is responsible for moving the button within the desired limits. The `Press Length` variable determines the limits of the button. When the button reaches the bottom and is pressed fully, the `Button Press Event` will be triggered. Additionally, there are two more events:

- `OnHapticFeedbackStarted`
- `OnHapticFeedbackStartAndEnd`

These events fire when the `Haptic Feedback` of the button is triggered.

The button also contains a `SpringJoint` and a `Rigidbody` component, which are Unity elements used to make the button behave more realistically.

The `Haptic Feedback` component is responsible for triggering the haptic feedback in the button.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/rb_lock.png" alt="Lock Rigodbody Zone Gameobject" width="400" />
  <p style="font-size: 14px; color: gray;">Figure 4: Lock Rigodbody Zone Gameobject</p>
</div>

The next significant GameObject containing logic is the `Lock Rigidbody Zone`.

The `Lock Rigidbody Zone` is responsible for locking the button when it is touched from underneath, preventing unintended movement. It contains the following:

- `InteractionDetector`
- `RigidbodyLocker`

The `InteractionDetector` is a highly useful component for creating simple interactions. It provides information when an item is touched and allows the selection of specific parts of the hand as contact points. For example, selecting `Finger_Tip` as the interaction part ensures that the interaction is triggered only when the item is touched with the fingertips.

The `InteractionDetector` includes the following two important events to expand interaction logic:

- `OnObjectStartedTouching`: Detects when the user starts touching an object.
- `OnObjectStoppedTouching`: Triggers when all fingers are removed from the object.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Button_bottom_locker_Collider.png" alt="Button_bottom_locker_Collider" width="400" />
  <p style="font-size: 14px; color: gray;">Figure 5: Collider on bottom of the button stopping the button from moving</p>
</div>

The `RigidbodyLocker` component works in conjunction with the `InteractionDetector`. It locks the `Rigidbody` when the interaction conditions defined in the `InteractionDetector` are met. This ensures the button remains stationary, even if the collider on the bottom of the button is touched.

---

## Haptikos Dimmer

The `Haptikos Dimmer` is a premade interactive component that allows the simulation of the rotation of a dimmer by grabbing and rotating its circular handle. This interaction provides precise feedback and control by delivering haptic feedback to the fingers upon contact with the dimmer and triggering haptic responses whenever the dimmer snaps to or passes an indication value.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Dimmer.png" alt="Haptikos_Dimmer" width="300" />
  <p style="font-size: 14px; color: gray;">Figure 1: Haptikos Dimmer</p>
</div>

### Haptikos Dimmer Hierarchy and Scripts

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Dimmer_Hierarchy.png" alt="aptikos_Dimmer_Hierarchy" width="300" />
  <p style="font-size: 14px; color: gray;">Figure 2: Haptikos Dimmer Hierarchy</p>
</div>

The `Haptikos Dimmer` contains the following scripts:

- `Haptikos Dimmer`
- `Dimmer Indicator`
- `Dimmer Handle`

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Dimmer_Scripts.png" alt="aptikos_Dimmer_Script" width="500" />
  <p style="font-size: 14px; color: gray;">Figure 3: Haptikos Dimmer Script</p>
</div>

The `Haptikos Dimmer` is the primary GameObject in the hierarchy responsible for handling user interaction with a virtual dimmer. It provides haptic feedback when interacting with the dimmer, triggering haptic events based on changes in the dimmer's rotation or indicator value. The dimmer controls the rotation of its handle and maps this rotation to specific dimmer values, ensuring precise control.

Additionally, the `Haptikos Dimmer` supports snapping functionality, aligning the handle to the nearest valid indicator value after interaction ends. It adjusts the handle's rotation dynamically based on the relative motion of the user's hand, enhancing interactivity.

A UnityEvent, `OnDimmerValueChanged`, is invoked whenever the dimmer value changes, allowing for external custom behaviors to be linked to these changes.

`Dimmer Indicator` script handles the behavior of the `Dimmer Indicator` in the Haptikos system. It detects collisions with objects named `Indication` and updates the slider value of the associated `Haptikos Dimmer` based on the parsed value from the collided object's name.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Dimmer_Handle_Script.png" alt="Dimmer_Handle_Script" width="500" />
  <p style="font-size: 14px; color: gray;">Figure 4: Dimmer Handle Script</p>
</div>

The `Dimmer Handle` script manages the interaction logic for grabbing and controlling the Haptikos Dimmer's handle. It ensures proper handling of grab events, validates interactions, and resets the handle state when necessary. Specifically, it detects when the handle is grabbed by validating that both a thumb and another finger are touching the handle and that all interacting fingers belong to the same hand.

It tracks the position and rotation of the dimmer handle relative to the user's hand and updates the handle's rotation based on the user's hand movement.

It also monitors for entering or exiting collisions with the user's fingers and triggers haptic feedback when fingers interact with the handle.

---

## Haptikos Table Switch

Another ready-made interactable object is a table switch.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Switch.png" alt="Haptikos Table Switch" width="400" />
  <p style="font-size: 14px; color: gray;">Figure 1: Haptikos Table Switch</p>
</div>

The `Haptikos Table Switch` contains the following hierarchy:

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/table_sw.png" alt="Haptikos_Table_Switch_Hierarchy" width="200" />
  <p style="font-size: 14px; color: gray;">Figure 2: Haptikos Table Switch Hierarchy</p>
</div>

### Haptikos Table Switch Hierarchy and Scripts

All the logic is contained in the `HandleRod` GameObject.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/state_changer.png" alt="state_changer" width="400" />
  <p style="font-size: 14px; color: gray;">Figure 3: The combination of scripts creating the switch</p>
</div>

The `Haptikos Table Switch` logic is a combination of 3 scripts:

- `StateChanger`
- `InteractionDetector`
- `InteractionDelayer`

The `StateChanger` script is used to control the On and Off states of a GameObject by transitioning it between specified positions. Both the start and end states of the GameObject are provided as inputs to the script. These states are visually highlighted in Figure 4 (color is used for demonstration purposes only).

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_ON_OFF_State.png" alt="Haptikos_ON_OFF_State" width="300" />
  <p style="font-size: 14px; color: gray;">Figure 4: On & Off State of the switch</p>
</div>

The `InteractionDelayer` script makes the interaction available again after a specified delay. In the case of the switch, this delay is set to 0.5 seconds. Without the `InteractionDelayer`, repeated touches on the object could trigger multiple interactions, making it difficult to control the interaction’s behavior. The `InteractionDelayer` prevents this issue by regulating interaction timing.

---

## Haptikos Wall Switch

The wall switch is similar to the normal switch but includes different scripts to introduce variation and relies solely on transform rotations to create a more realistic and immersive experience for the user.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Wall_Switch.png" alt="Haptikos_Wall_Switch" width="300" />
  <p style="font-size: 14px; color: gray;">Figure 1: Haptikos Wall Switch</p>
</div>

### Haptikos Wall Switch Hierarchy and Scripts

The hierarchy of the `Haptikos Wall Switch` is the following:

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Wall_Switch_Hierarchy.png" alt="" width="300" />
  <p style="font-size: 14px; color: gray;">Figure 2: Haptikos Wall Switch Hierarchy</p>
</div>

It also contains the following scripts:
- `Haptikos_SwitchButton`
- `HapticFeedback`
- `Haptikos_SwitchButtonArea`

The `Haptikos Wall Switch` script determines whether it is in the On or Off state and then adjusts the visibility of the corresponding collider accordingly. The collider plays a crucial role in the `Haptikos_SwitchButtonArea` script (contained within the `Area1` and `Area2` GameObjects). This script triggers the `OnTriggerEnter` function when touched, updating the `Haptikos_SwitchButton` script to toggle the switch's state between On and Off.

---

## Haptikos Lever

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Lever.png" alt="Haptikos_Lever" width="300" />
  <p style="font-size: 14px; color: gray;">Figure 1: Haptikos Lever</p>
</div>

Due to its complexity, the lever uses `Unity Physics` more than the other components. It uses a hinge joint to connect 2 GameObjects and limits where the object can rotate. Learn more about hinge joints [here](https://docs.unity3d.com/Manual/class-HingeJoint.html).

### Haptikos Lever Hierarchy and Scripts

The hierarchy of the lever can be seen here:

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Lever_Hierarchy.png" alt="Haptikos Lever Hierarchy" width="200" />
  <p style="font-size: 14px; color: gray;">Figure 2: Haptikos Lever Hierarchy</p>
</div>

Some GameObjects of the hierarchy only contain models, while others also contain scripts or Unity components. The base of the `Haptikos Lever` contains the `Hinge Joint` which is responsible for connecting the `Base` and the `HandleRod` GameObjects.

The lever contains the following scripts:

- `Haptikos_Lever`
- `LeverHandle`
- `LeverRod`
- `HapticFeedback`

#### Haptikos Lever

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Lever_Script.png" alt="Haptikos Lever Script" width="400" />
  <p style="font-size: 14px; color: gray;">Figure 3: Haptikos Lever Script</p>
</div>

The `Haptikos Lever` is at the top object of the hierarchy and it is responsible for providing the `OnLeverValueEvent`, which can be utilized to understand where the `Haptikos Lever` is compared to its limits. It uses the Limits of the `Hinge Joint` to calculate the starting and final position of the lever.

#### Lever Handle

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Lever_Handle_Script.png" alt="Lever_Handle_Script" width="700" />
  <p style="font-size: 14px; color: gray;">Figure 4: Lever Handle Script</p>
</div>

The `Lever Handle` facilitates interaction with a virtual lever by allowing the user to grab and move the lever handle. Upon being grabbed, the lever attaches to the user’s hand, and when moved beyond a certain threshold, it snaps back to its original position, effectively simulating the behavior of a physical lever mechanism.

The LeverHandle also takes into account `HapticFeedback` since it is a `HapticItem` and triggers the haptic feedback when the user is in the position to move the lever.

#### Lever Rod

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Lever_Rod_Script.png" alt="Lever_Rod_Script" width="400" />
  <p style="font-size: 14px; color: gray;">Figure 5: Lever Rod Script</p>
</div>

The `Lever Rod` script uses the position of the lever as input and applies it to the rod, enabling movement that aligns with both the `Hinge Joint` and the user's hand movement. This ensures a more realistic and seamless interaction.

---

## Haptikos Slider

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Slider.png" alt="Haptikos_Slider" width="200" />
  <p style="font-size: 14px; color: gray;">Figure 1: Haptikos Slider</p>
</div>

The slider also doesn’t rely on physics for its functionality; it can be used as a tool to increase or decrease values for certain applications.

### Haptikos Slider Hierarchy and Scripts

The `Haptikos Slider` has the following hierarchy:

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Slider_Hierarchy.png" alt="Haptikos_Slider_Hierarchy" width="400" />
  <p style="font-size: 14px; color: gray;">Figure 2: Haptikos Slider Hierarchy</p>
</div>

The slider has the following scripts:

- `Haptikos_Slider`
- `SliderHapticFeedbackHandler`
- `HapticFeedback`
- `HandDetector`

#### Haptikos Slider

First of all, `Haptikos_Slider` is the main component and it gives out two Unity Events:

- `OnSliderValueChanged`
- `OnSliderSnap`

The `OnSliderValueChanged` event is invoked when the slider changes value and it also gives out the value of the new slider location.

`OnSliderSnap` invokes when the slider snaps to a different value, without giving a value, just by indicating that the Slider changed location.

The `Haptikos_Slider` handles the logic required for interacting with the slider. It requires at least one finger and the thumb to grab the slider. Once held, the slider can be moved up and down by adjusting the hand's position. As the slider is moved, it snaps to the nearest indication value (e.g., 20) when within proximity. If the hand moves away beyond the acceptable grab distance, the slider must be grabbed again to continue interaction.

#### SliderHapticFeedbackHandler

The next scripts are located in the `Moving_Handle` GameObject.

The `SliderHapticFeedbackHandler` manages the `HapticFeedback` script and logic for the slider. Haptic feedback is triggered when the slider is grabbed and when the slider snaps to a new indication. This script relies on the `HandDetector` script and the `OnTriggerEnter` function to detect when the handle is touched.

#### HandDetector

The `HandDetector` is a general-purpose script that detects which hand is closest to a specified object. It provides customization for defining the acceptable distance for a hand to be considered close enough and configuring the number of fingers detected for object manipulation. The script has the following events:

- `OnHandWithinAcceptableDistance`
- `OnFingerWithinAcceptableDistance`

These events trigger when the user's hand and fingers are within an acceptable distance of the object.

---

## Haptikos Grabbable Object

The final interactable component, called `Grabbable`, is designed to be used as an object that can be grabbed using the exoskeletons. The SDK contains an example grabbable object—a cube—but any object intended for manipulation can be assigned as a grabbable.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/grab.png" alt="grab" width="400" />
  <p style="font-size: 14px; color: gray;">Figure 1: Haptikos Grabbable Object Example</p>
</div>

### Haptikos Grabbable Object Scripts

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Grabbable.png" alt="Grabbable" width="600" />
  <p style="font-size: 14px; color: gray;">Figure 2: Haptikos Grabbable Object Scripts</p>
</div>

The `Grabbable` contains two scripts:

- `Haptikos_Grab`
- `HapticFeedback`


#### Haptikos Grab

The `Haptikos_Grab` component includes a boolean property named `Palm Needed`. When set to true, the user must use their palm to grab the GameObject. The `Haptikos_Grab` script creates a clone of the grabbable object that is slightly larger (a 10% increase in size). This ensures the object gives the illusion that fingers do not pass through it when grabbed. Additionally, the script clones the object’s collider (preferably a mesh collider), marks it as a trigger, and attaches a script called `Haptikos_Clone_Grab` to the cloned object. This script handles all the grab logic for the interaction.

#### Haptikos Clone Grab

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Grabbable_Clone_Grab.png" alt="Grabbable_Clone_Grab" width="400" />
  <p style="font-size: 14px; color: gray;">Figure 3: Haptikos Grabbable Object Clone Creation</p>
</div>

The `Haptikos_Clone_Grab` script determines which fingers are touching the object by using the `OnTriggerEnter` function. If the thumb and at least one additional finger are detected, the object is grabbed and becomes a child of the hand currently interacting with it.

The `Grabbable` object is highly customizable. Its appearance can be modified by changing the mesh of the GameObject, or the script can be attached to any GameObject to make it grabbable.