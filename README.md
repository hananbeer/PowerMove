# PowerMove

**PowerMove** is a Blender add-on for rapid animation.

Power up your workflow with **PowerMove**!

*Buy it soon on [Blender Market](https://blendermarket.com)!*

# Installation

Download this repo as a zip file.

In Blender go to Edit -> Preferences -> Add-ons and install from the zip file.

Make sure the add-on is enabled.

# Usage

*NOTE: This add-on is assigned to the `G` key. You may change that in the settings, or simply disable the plugin to restore the original functionality.*

*NOTE 2: For now the hotkey `G` is only registered for Pose mode, but you can still call `transform.powermove` if you want and register a hotkey for that in other modes as well or even globally.*

Press `G` to enter **PowerMove** mode. In this mode you may drag to move with the `Left Mouse` down, drag to rotate with the `Right Mouse` down and trackball rotation with `Alt + Right Mouse`.

You may also use standard actions such as locking to specific axis, plane, snapping and so on.

To switch objects or bones press `Alt + Left Mouse`. This can be combined with standard Blender actions such, e.g. `Alt + Shift + Left Mouse` to add an object or bone to the selection (or deselect if it is already the active object or bone). If you want to box select or some other action you should leave **PowerMove** mode by either pressing `Esc` or double-clicking.

You can also switch between rotation, trackball, translation and scale. Note that if you do that, you should end the action with `Alt + Left Click` due to technical limitations of the Blender API. Generally if you encounter issues, use `Alt + Left Click` to go back to **PowerMove** mode, `Ctrl + Z` to undo some previous actions or `Esc` to exit **PowerMove** mode.

# Known bugs

- Some Blender versions don't really disable the add-on when unticking in Edit -> Preferences -> Add-ons; but you can restarting Blender if that happens.
- Changing modes does not leave **PowerMove** mode.

# Contact

Feel free to contact me for feedback, feature requests, support, etc.

The best way to contact me is [@high_byte](https://twitter.com/high_byte) on Twitter.

# License

GPLv3
