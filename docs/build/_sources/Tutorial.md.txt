# Tutorial: Building a Scene with Haptikos

This tutorial guides you through the process of setting up a basic scene in Unity using the `Haptikos Panel`, which provides quick access to all premade assets.

#### Step 1: 

Create an Empty Unity Scene:

- Start by creating an empty Unity scene.
- Delete the main camera from the scene to prepare for custom Haptikos setup.

#### Step 2: 

Access the `Haptikos Panel`:

- Click the `Haptikos` button on the Unity toolbar.
- Open the `Haptikos Panel` to access various premade assets and tools for your scene.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Panel.png" alt="Haptikos_Gesture_Select" width="200" />
  <p style="font-size: 14px; color: gray;">Figure 1: Haptikos Panel</p>
</div>

#### Step 3:

 Click on the `Haptikos Player` button to bring an instance of the `HaptikosPlayer` into the scene.

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Panel_Player.png" alt="Haptikos_Gesture_Select" width="200" />
  <p style="font-size: 14px; color: gray;">Figure 2: Haptikos Player Panel</p>
</div>

#### Step 4: 

<div style="text-align: center; margin-top: 10px; margin-bottom: 10px;">
  <img src="_static/Haptikos_Item_Panel.png" alt="Haptikos_Gesture_Select" width="150" />
  <p style="font-size: 14px; color: gray;">Figure 3: Haptikos Item Panel</p>
</div>

Click on any of the buttons to bring an instance of the prefab into the scene.

All the prefabs in the categories `Haptikos Assets`, `Grabbable 3D Assets` and `Advanced Premade Haptik Items` are game object that can be interacted with by touch and are described in the `Interaction Pieces` Section. 


The `Haptikos Gesture` prefabs category includes the `Gesture Recognizer` prefab and some ready to go components of the `Raycast` system. For more information go to `Gestures` section.


Setting up the raycast system and using the premade selectables is straightforward. Either select the raycast menu prefab or any of the raycasters. Then click on any of the ready to go selectables.


The ready to go selectables 
- `Teleport Area`: Ground Area that allows the player to teleport around using the teleport raycast 


- `FollowRay`: Attach to any game object with a collider and rigidbody. Then the user will be able to move it around using the cursor raycast 
`Canvas` and button prefabs: Drag the `Canvas` into the scene and add buttons as its children. These buttons can then be treated as standard Unity UI buttons, interactable through both the cursor raycast and the hand models. 


The `HaptikosCanvas` and `HaptikosSelectableButton` scripts attached to the canvas and button respectively allow you to resize the colliders automatically to fit the size of the UI elements. 


The extras category:

- `Teleporter`: A small area to be teleported on, useful to make only certain parts of the ground available for teleport.

- `Portal`: When touched by any of the hand models, load into the scene indicated by the Scene Number variable of the attached `PortalSceneLoader` script.
