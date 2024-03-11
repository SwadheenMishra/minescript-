# SPDX-FileCopyrightText: © 2022-2024 Greg Christiana <maxuser@minescript.net>
# SPDX-License-Identifier: GPL-3.0-only

# WARNING: This file is generated from the Minescript jar file. This file will
# be overwritten automatically when Minescript updates to a new version. If you
# make edits to this file, make sure to save a backup copy when upgrading to a
# new version of Minescript.

"""minescript v4.0 distributed via Minescript jar file

Usage: import minescript  # from Python script

User-friendly API for scripts to make function calls into the
Minescript mod.  This module should be imported by other
scripts and not run directly.
"""

import asyncio
import base64
import os
import queue
import sys
import minescript_runtime

from array import array
from minescript_runtime import (
    await_script_function,
    call_async_script_function,
    send_script_function_request,
    ExceptionHandler)
from typing import Any, List, Set, Dict, Tuple, Optional, Callable, Awaitable


def execute(command: str):
  """Executes the given command.

  If `command` doesn't already start with a slash or backslash, automatically
  prepends a slash. Ignores leading and trailing whitespace, and ignores empty
  commands.

  *Note: This was named `exec` in Minescript 2.0. The old name is no longer
  available in v3.0.*

  Since: v2.1
  """
  command = command.strip()
  if not command:
    return
  if command[0] not in ("/", "\\"):
    command = "/" + command
  print(command)


def echo(message: Any):
  """Echoes message to the chat.

  The echoed message is visible only to the local player.

  Since: v2.0
  """
  print(message, file=sys.stderr)


def chat(message: str):
  """Sends the given message to the chat.

  If `message` starts with a slash or backslash, automatically prepends a space
  so that the message is sent as a chat and not executed as a command.  Ignores
  empty messages.

  Since: v2.0
  """
  if not message:
    return
  # If the message starts with a slash or backslash, prepend a space so that
  # the message is printed and not executed as a command.
  if message[0] in ("/", "\\"):
    message = " " + message
  print(message)

def set_player_gamemode(gm: str) -> bool:
  await_script_function("set_player_gamemode", (gm,))


def player_interact_at(x: int, y: int, z: int, offHand=False) -> bool:
    await_script_function("player_interact_at", (x, y, z, offHand))

def player_interact_item(offHand=False) -> bool:
    await_script_function("player_interact_item", (offHand,))

def get_player(nbt=False) -> dict:
    return await_script_function("get_player", (nbt,))

def set_player_fov(f: float) -> bool:
    await_script_function("set_player_fov", (f, ))

def player_start_break_block(x, y, z):
    await_script_function("player_start_break_block", (x, y, z))

def player_continue_break_block(x, y, z):
    await_script_function("player_continue_break_block", (x, y, z))

def player_stop_break_block():
    await_script_function("player_stop_break_block", ())

def log(message: str) -> bool:
  """Sends the given message to latest.log.

  Args:
    message: string to send to the log

  Returns:
    `True` if `message` was logged successfully.

  Since: v3.0
  """
  if not message:
    return
  await_script_function("log", (message,))


def screenshot(filename=None):
  """Takes a screenshot, similar to pressing the F2 key.

  Args:
    filename: if specified, screenshot filename relative to the screenshots directory; ".png"
      extension is added to the screenshot file if it doesn't already have a png extension.

  Since: v2.1
  """
  if filename is None:
    await_script_function("screenshot", (None,))
    return

  if os.path.sep in filename:
    raise Exception(f'`screenshot` does not support filenames with "{os.path.sep}" character.')

  if not filename.lower().endswith(".png"):
    filename += ".png"
  await_script_function("screenshot", (filename,))


def flush():
  """Wait for all previously issued script commands from this job to complete.

  Since: v2.1
  """
  return await_script_function("flush", ())

def player_attack_entity(uuid: str):
  return await_script_function("player_attack_entity", (uuid,))


def player_name() -> str:
  """Gets the local player's name.

  Since: v2.1
  """
  return await_script_function("player_name", ())


def player_position() -> List[float]:
  """Gets the local player's position.

  Returns:
    player's position as [x: float, y: float, z: float]

  Update in v4.0:
    Removed `done_callback` arg. Use `async_player_position()` for async execution.
  """
  return await_script_function("player_position", ())


def async_player_position() -> Awaitable[List[float]]:
  """Gets the local player's position.

  Similar to `player_position()`, but can be used with `await` and `asyncio`.

  Returns:
    awaitable position of player as [x: float, y: float, z: float]

  Since: v4.0
  """
  return call_async_script_function("player_position", ())


def player_set_position(
    x: float, y: float, z: float, yaw: float = None, pitch: float = None) -> bool:
  """Sets the player's position, and optionally orientation.

  Note that in survival mode the server may reject the new coordinates if they're too far
  or require moving through walls.

  Args:
    x, y, z: position to try to move player to
    yaw, pitch: if not None, player's new orientation

  Since: v3.1
  """
  return await_script_function("player_set_position", (x, y, z, yaw, pitch))

def get_distance(P1: list, P2: list) -> str:
  x, y, z = P1
  x2, y2, z2 = P2
  return await_script_function("get_distance", (x, y, z, x2, y2, z2))

def get_online_players() -> dict:
  return await_script_function("get_online_players", ())

def player_remove_gravity(g: bool) -> bool:
  return await_script_function("player_remove_gravity", (g, ))

def player_swing_hand(h=False) -> bool:
  return await_script_function("player_swing_hand", (h, ))

def player_get_vehicle() -> dict | bool:
    return await_script_function("player_get_vehicle", ())

def player_add_velocity(
    x: float, y: float, z: float) -> bool:
    return await_script_function("player_add_velocity", (x, y, z))

def player_set_velocity(
    x: float, y: float, z: float) -> bool:
    return await_script_function("player_set_velocity", (x, y, z))

def player_set_vehicle_velocity(
    x: float, y: float, z: float) -> bool:
    return await_script_function("player_set_vehicle_velocity", (x, y, z))

def player_set_strinting(x: bool) -> bool:
    return await_script_function("player_set_sprinting", (x,))

def async_player_set_position(
    x: float, y: float, z: float, yaw: float = None, pitch: float = None) -> Awaitable[bool]:
  """Sets the player's position, and optionally orientation.

  Note that in survival mode the server may reject the new coordinates if they're too far
  or require moving through walls.

  Similar to `player_set_position(...)`, but can be used with `await` and `asyncio`.

  Args:
    x, y, z: position to try to move player to
    yaw, pitch: if not None, player's new orientation

  Since: v4.0
  """
  return call_async_script_function("player_set_position", (x, y, z, yaw, pitch))


def player_hand_items() -> List[Dict[str, Any]]:
  """Gets the items in the local player's hands.

  Returns:
    Items in player's hands as a list of items where each item is a dict:
    `{"item": str, "count": int}`, plus `"nbt": str` if the item has NBT data;
    main-hand item is at list index 0, off-hand item at index 1.

  Update in v4.0:
    Removed `done_callback` arg. Use `async_player_hand_items()` for async execution.

  Since: v2.0
  """
  return await_script_function("player_hand_items", ())

def player_jump() -> bool:
  return await_script_function("player_jump", ())

def async_player_hand_items() -> Awaitable[List[Dict[str, Any]]]:
  """Gets the items in the local player's hands.

  Returns:
    Awaitable items in player's hands as a list of items where each item is a
    dict: `{"item": str, "count": int}`, plus `"nbt": str` if the item has NBT
    data; main-hand item is at list index 0, off-hand item at index 1.

  Similar to `player_hand_items()`, but can be used with `await` and `asyncio`.

  Since: v4.0
  """
  return call_async_script_function("player_hand_items", ())


def player_inventory() -> List[Dict[str, Any]]:
  """Gets the items in the local player's inventory.

  Returns:
    Items in player's inventory as list of items where each item is a dict:
    `{"item": str, "count": int, "slot": int}`, plus `"nbt": str` if an item
    has NBT data and `"selected": True` for the item selected in the player's
    main hand.

  Update in v4.0:
    Removed `done_callback` arg. Use `async_player_inventory()` for async execution.

  Update in v3.0:
    Introduced `"slot"` and `"selected"` attributes in the returned
    dict, and `"nbt"` is populated only when NBT data is present. (In prior
    versions, `"nbt"` was always populated, with a value of `null` when NBT data
    was absent.)

  Since: v2.0
  """
  return await_script_function("player_inventory", ())


def async_player_inventory() -> Awaitable[List[Dict[str, Any]]]:
  """Gets the items in the local player's inventory.

  Similar to `player_inventory()`, but can be used with `await` and `asyncio`.

  Returns:
    Awaitable items in player's inventory as list of items where each item is a
    dict: `{"item": str, "count": int, "slot": int}`, plus `"nbt": str` if an
    item has NBT data and `"selected": True` for the item selected in the
    player's main hand.

  Since: v4.0
  """
  return call_async_script_function("player_inventory", ())


def player_inventory_slot_to_hotbar(slot: int) -> int:
  """Swaps an inventory item into the hotbar.

  Args:
    slot: inventory slot (9 or higher) to swap into the hotbar

  Returns:
    hotbar slot (0-8) into which the inventory item was swapped

  Update in v4.0:
    Removed `done_callback` arg. Use `async_player_inventory_slot_to_hotbar(...)
    for async execution.

  Since: v3.0
  """
  return await_script_function("player_inventory_slot_to_hotbar", (slot,))


def async_player_inventory_slot_to_hotbar(slot: int) -> Awaitable[int]:
  """Swaps an inventory item into the hotbar.

  Similar to `player_inventory_slot_to_hotbar(...)`, but can be used with `await` and `asyncio`.

  Args:
    slot: inventory slot (9 or higher) to swap into the hotbar

  Returns:
    awaitable hotbar slot (0-8) into which the inventory item is swapped

  Since: v4.0
  """
  return call_async_script_function("player_inventory_slot_to_hotbar", slot)


def player_inventory_select_slot(slot: int) -> int:
  """Selects the given slot within the player's hotbar.

  Args:
    slot: hotbar slot (0-8) to select in the player's hand

  Returns:
    previously selected hotbar slot

  Update in v4.0:
    Removed `done_callback` arg. Use `async_player_inventory_select_slot(...)` for async execution.

  Since: v3.0
  """
  return await_script_function("player_inventory_select_slot", (slot,))


def async_player_inventory_select_slot(slot: int) -> Awaitable[int]:
  """Selects the given slot within the player's hotbar.

  Similar to `player_inventory_select_slot(...)`, but can be used with `await` and `asyncio`.

  Args:
    slot: hotbar slot (0-8) to select in the player's hand

  Returns:
    awaitable of previously selected hotbar slot

  Since: v4.0
  """
  return call_async_script_function("player_inventory_select_slot", slot)


def player_press_forward(pressed: bool):
  """Starts/stops moving the local player forward, simulating press/release of the 'w' key.

  Args:
    pressed: if `True`, go forward, otherwise stop doing so

  Since: v2.1
  """
  return await_script_function("player_press_forward", (pressed,))


def player_press_backward(pressed: bool):
  """Starts/stops moving the local player backward, simulating press/release of the 's' key.

  Args:
    pressed: if `True`, go backward, otherwise stop doing so

  Since: v2.1
  """
  return await_script_function("player_press_backward", (pressed,))


def player_press_left(pressed: bool):
  """Starts/stops moving the local player to the left, simulating press/release of the 'a' key.

  Args:
    pressed: if `True`, move to the left, otherwise stop doing so

  Since: v2.1
  """
  return await_script_function("player_press_left", (pressed,))


def player_press_right(pressed: bool):
  """Starts/stops moving the local player to the right, simulating press/release of the 'd' key.

  Args:
    pressed: if `True`, move to the right, otherwise stop doing so

  Since: v2.1
  """
  return await_script_function("player_press_right", (pressed,))


def player_press_jump(pressed: bool):
  """Starts/stops the local player jumping, simulating press/release of the space key.

  Args:
    pressed: if `True`, jump, otherwise stop doing so

  Since: v2.1
  """
  return await_script_function("player_press_jump", (pressed,))


def player_press_sprint(pressed: bool):
  """Starts/stops the local player sprinting, simulating press/release of the left control key.

  Args:
    pressed: if `True`, sprint, otherwise stop doing so

  Since: v2.1
  """
  return await_script_function("player_press_sprint", (pressed,))


def player_press_sneak(pressed: bool):
  """Starts/stops the local player sneaking, simulating press/release of the left shift key.

  Args:
    pressed: if `True`, sneak, otherwise stop doing so

  Since: v2.1
  """
  return await_script_function("player_press_sneak", (pressed,))


def player_press_pick_item(pressed: bool):
  """Starts/stops the local player picking an item, simulating press/release of the middle mouse button.

  Args:
    pressed: if `True`, pick an item, otherwise stop doing so

  Since: v2.1
  """
  return await_script_function("player_press_pick_item", (pressed,))


def player_press_use(pressed: bool):
  """Starts/stops the local player using an item or selecting a block, simulating press/release of the right mouse button.

  Args:
    pressed: if `True`, use an item, otherwise stop doing so

  Since: v2.1
  """
  return await_script_function("player_press_use", (pressed,))


def player_press_attack(pressed: bool):
  """Starts/stops the local player attacking or breaking a block, simulating press/release of the left mouse button.

  Args:
    pressed: if `True`, press attack, otherwise stop doing so

  Since: v2.1
  """
  return await_script_function("player_press_attack", (pressed,))


def player_press_swap_hands(pressed: bool):
  """Starts/stops moving the local player swapping hands, simulating press/release of the 'f' key.

  Args:
    pressed: if `True`, swap hands, otherwise stop doing so

  Since: v2.1
  """
  return await_script_function("player_press_swap_hands", (pressed,))


def player_press_drop(pressed: bool):
  """Starts/stops the local player dropping an item, simulating press/release of the 'q' key.

  Args:
    pressed: if `True`, drop an item, otherwise stop doing so

  Since: v2.1
  """
  return await_script_function("player_press_drop", (pressed,))


def player_orientation():
  """Gets the local player's orientation.

  Returns:
    (yaw: float, pitch: float) as angles in degrees

  Since: v2.1
  """
  return await_script_function("player_orientation", ())


def player_set_orientation(yaw: float, pitch: float):
  """Sets the local player's orientation.

  Args:
    yaw: degrees rotation of the local player's orientation around the y axis
    pitch: degrees rotation of the local player's orientation from the x-z plane

  Returns:
    True if successful

  Since: v2.1
  """
  return await_script_function("player_set_orientation", (yaw, pitch))


def player_get_targeted_block(max_distance: float = 20):
  """Gets info about the nearest block, if any, in the local player's crosshairs.

  Args:
    max_distance: max distance from local player to look for blocks

  Returns:
    [[x, y, z], distance, side, block_description] if the local player has a
    block in their crosshairs within `max_distance`, `None` otherwise.
    `distance` (float) is calculated from the player to the targeted block;
    `side` (str) is the direction that the targeted side of the block is facing
    (e.g. `"east"`); `block_description` (str) describes the targeted block.

  Since: v3.0
  """
  return await_script_function("player_get_targeted_block", (max_distance,))

def player_get_targeted_entity(max_distance: float = 20, nbt=False):
  return await_script_function("player_get_targeted_entity", (max_distance, nbt))


def player_health() -> float:
  """Gets the local player's health.

  Since: v3.1
  """
  return await_script_function("player_health", ())


def players(*, nbt: bool = False):
  """Gets a list of nearby players and their attributes.

  Args:
    nbt: if `True`, populate an `"nbt"` attribute for each returned player

  Returns:
    List of players where each player is represented as a dict containing:
    `"name": str, "health": float, "type": str,
    "position": [float, float, float], "yaw": float, "pitch": float,
    "velocity": [float, float, float]`. The local player has the attribute
    `"local": True`. The`"nbt"` attribute is present if `nbt` arg is `True`.

  Update in v3.1:
    Added `"health"` and `"local"` attributes, and `nbt` arg to output `"nbt"`
    attribute.

  Since: v2.1
  """
  return await_script_function("players", (nbt,))

def send_packet(PacketName: str, Value=None):
    '''
    onGround: bool
    '''
    await_script_function("send_packet", (PacketName, Value))

def entities(*, nbt: bool = False):
  """Gets a list of nearby entities and their attributes.

  Args:
    nbt: if `True`, populate an `"nbt"` attribute for each returned entity

  Returns:
    List of entities where each entity is represented as a dict containing:
    `"name": str, "health": float (living entities only), "type": str,
    "position": [float, float, float], "yaw": float, "pitch": float,
    "velocity": [float, float, float]`. Living entities have
    `"health": float` and the local player has `"local": True`. The`"nbt"`
    attribute is present if `nbt` arg is `True`.

  Update in v3.1:
    Added `"health"` and `"local"` attributes, and `nbt` arg to output `"nbt"`
    attribute.

  Since: v2.1
  """
  return await_script_function("entities", (nbt,))


def world_properties() -> Dict[str, Any]:
  """Gets world properties.

  If the current world is a multiplayer world loaded from the server list, then
  the returned `name` and `address` attributes are the values as they appear in
  the server list; otherwise `name` is the name of the locally saved world and
  `address` is `localhost`.

  `"day_ticks"` are the ticks associated with the day-night cycle.

  Returns:
    Dict containing: `"game_ticks": int, "day_ticks": int, "raining": bool,
    "thundering": bool, "spawn": BlockPos, "hardcore": bool,
    "difficulty": str, "name": str, "address": str`

  Since: v3.1
  """
  return await_script_function("world_properties", ())


def getblock(x: int, y: int, z: int) -> str:
  """Gets the type of block at position (x, y, z).

  Args:
    x, y, z: position of block to get

  Returns:
    block type at (x, y, z) as a string
  """
  return await_script_function("getblock", (x, y, z))


def async_getblock(x: int, y: int, z: int) -> Awaitable[str]:
  """Gets the type of block at position (x, y, z).

  Similar to `getblock(...)`, but can be used with `await` and `asyncio`.

  Args:
    x, y, z: position of block to get

  Returns:
    awaitable block type at (x, y, z) as a string

  Since: v4.0
  """
  return call_async_script_function("getblock", (x, y, z))


def getblocklist(positions: List[List[int]]) -> List[str]:
  """Gets the types of block at the specified [x, y, z] positions.

  Args:
    list of positions as lists of x, y, z int coordinates, e.g. [[0, 0, 0], [0, 0, 1]]

  Returns:
    block types at given positions as list of strings

  Update in v4.0:
    Removed `done_callback` arg. Use `async_getblocklist(...)` for async execution.

  Since: v2.1
  """
  return await_script_function("getblocklist", (positions,))


def async_getblocklist(positions: List[List[int]]) -> Awaitable[List[str]]:
  """Gets the types of block at the specified [x, y, z] positions.

  Similar to `getblocklist(...)`, but can be used with `await` and `asyncio`.

  Args:
    awaitable list of positions as lists of x, y, z int coordinates, e.g. [[0, 0, 0], [0, 0, 1]]

  Returns:
    awaitable block types at given positions as list of strings

  Since: v4.0
  """
  return call_async_script_function("getblocklist", (positions,))


def await_loaded_region(x1: int, z1: int, x2: int, z2: int, timeout: float = None) -> bool:
  """Waits for chunks to load in the region from (x1, z1) to (x2, z2).

  Args:
    x1, z1, x2, z2: bounds of the region for awaiting loaded chunks
    timeout: if specified, timeout in seconds to wait for the region to load

  Returns:
    `True` if the requested region has fully loaded.

  Update in v4.0:
    Removed `done_callback` arg. Call now always blocks until region is loaded
    or timeout (if specified) is reached.
  """
  try:
    return await_script_function("await_loaded_region", (x1, z1, x2, z2), timeout=timeout)
  except TimeoutError:
    return False


class EventRegistrationHandler:
  """Base class for event registration handlers. (__internal__)

  Since: v4.0
  """

  def __init__(self, register, registration_func, unregistration_func):
    """Creates an event registration handler.

    Args:
      register: if `True`, register the handler upon construction
    """
    self.queue = queue.Queue()
    self.registered = False
    self.registration_func = registration_func
    self.unregistration_func = unregistration_func
    if register:
      self.register()

  def register(self) -> bool:
    if self.registered:
      return False
    self.registration_func(self.queue.put, self.queue.put)
    self.registered = True
    return True

  def unregister(self) -> bool:
    if not self.registered:
      return False
    self.unregistration_func()
    self.registered = False
    return True

  def get(self, block: bool = True, timeout: float = None) -> Any:
    """Gets the next event in the queue.

    Args:
      block: if `True`, block until an event fires
      timeout: timeout in seconds to wait for an event if `block` is `True`

    Returns:
      subclass-dependent event

    Raises:
      `queue.Empty` if `block` is `True` and `timeout` expires, or `block` is `False` and
      queue is empty.
    """
    value = self.queue.get(block, timeout)
    if isinstance(value, Exception):
      raise value
    return value

  def __enter__(self):
    self.register()
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.unregister()

  def __del__(self):
    self.unregister()


class KeyEventListener(EventRegistrationHandler):
  """Listener for keyboard events.

  Only one `KeyEventListener` can be instantiated at a time within a job. For a
  list of key codes, see: https://www.glfw.org/docs/3.4/group__keys.html

  Inherits `register()` and `unregister()` methods from the base class,
  `EventRegistrationHandler`. These methods both return `bool` indicating
  whether the operation succeeded. Calling `register()` on a listener that's
  already registered returns `False`, and similarly for calling `unregister()`
  on a listener that's already unregistered.

  Implements context management so that it can be used with a `with` expression
  to automatically unregister the listener at the end of the block, e.g.

  ```
  events = []
  with KeyEventListener() as listener:
    # Listen for next 3 key events:
    for i in range(3):
      events.append(listener.get())

  # listener no longer registered here...
  ```

  Update in v4.0:
    Addition of `register()`, `unregister()`, and context management via `with` expression.

  Since: v3.2
  """

  def __init__(self, register=True):
    """Creates a `KeyEventListener` for listening to keyboard events.

    Args:
      register: if `True`, register the listener upon construction

    Update in v4.0:
      Added optional arg `register`.
    """
    super().__init__(register, register_key_event_listener, unregister_key_event_listener)

  def get(self, block: bool = True, timeout: float = None) -> Dict[str, Any]:
    """Gets the next key event in the queue.

    Args:
      block: if `True`, block until an event fires
      timeout: timeout in seconds to wait for an event if `block` is `True`

    Returns:
      event dict: `{"key": int, "scanCode": int, "action": int, "modifiers": int,
      "timeMillis": int, "screen": str}` where `action` is 0 for key up, 1 for
      key down, and 2 for key repeat.

    Raises:
      `queue.Empty` if `block` is `True` and `timeout` expires, or `block` is `False` and
      queue is empty.
    """
    return super().get(block, timeout)


def register_key_event_listener(
    listener: Callable[[str], None], exception_handler: ExceptionHandler = None):
  """Registers a listener for receiving keyboard events. One listener allowed per job.

  For a more user-friendly API, use `KeyEventListener` instead. (__internal__)

  Args:
    listener: callable that repeatedly accepts a string representing key events
    exception_handler: callable for handling an `Exception` thrown from Java (optional)

  Since: v3.2
  """
  send_script_function_request("register_key_event_listener", (), listener, exception_handler)


def unregister_key_event_listener():
  """Unregisters a key event listener, if any, for the currently running job.

  For a more user-friendly API, use `KeyEventListener` instead. (__internal__)

  Returns:
    `True` if successfully unregistered a listener.

  Since: v3.2
  """
  await_script_function("unregister_key_event_listener", ())


class MouseEventListener(EventRegistrationHandler):
  """Listener for mouse click events.

  Only one `MouseEventListener` can be instantiated at a time within a job.

  Inherits `register()` and `unregister()` methods from the base class,
  `EventRegistrationHandler`. These methods both return `bool` indicating
  whether the operation succeeded. Calling `register()` on a listener that's
  already registered returns `False`, and similarly for calling `unregister()`
  on a listener that's already unregistered.

  Implements context management so that it can be used with a `with` expression
  to automatically unregister the listener at the end of the block, e.g.

  ```
  events = []
  with MouseEventListener() as listener:
    # Listen for next 3 mouse events:
    for i in range(3):
      events.append(listener.get())

  # listener no longer registered here...
  ```

  Since: v4.0
  """

  def __init__(self, register=True):
    """Creates a `MouseEventListener` for listening to mouseboard events.

    Args:
      register: if `True`, register the listener upon construction
    """
    super().__init__(register, register_mouse_event_listener, unregister_mouse_event_listener)

  def get(self, block: bool = True, timeout: float = None) -> Dict[str, Any]:
    """Gets the next mouse event in the queue.

    Args:
      block: if `True`, block until an event fires
      timeout: timeout in seconds to wait for an event if `block` is `True`

    Returns:
      event dict: `{"button": int, "action": int, "modifiers": int,
      "timeMillis": int, "screen": str, "x": float, "y": float}` where `action`
      is 0 for mouse up and 1 for mouse down.

    Raises:
      `queue.Empty` if `block` is `True` and `timeout` expires, or `block` is `False` and
      queue is empty.
    """
    return super().get(block, timeout)


def register_mouse_event_listener(
    listener: Callable[[str], None], exception_handler: ExceptionHandler = None):
  """Registers a listener for receiving mouse events. One listener allowed per job.

  For a more user-friendly API, use `MouseEventListener` instead. (__internal__)

  Args:
    listener: callable that repeatedly accepts a string representing mouse events
    exception_handler: callable for handling an `Exception` thrown from Java (optional)

  Since: v4.0
  """
  send_script_function_request("register_mouse_event_listener", (), listener, exception_handler)


def unregister_mouse_event_listener():
  """Unregisters a mouse event listener, if any, for the currently running job.

  For a more user-friendly API, use `MouseEventListener` instead. (__internal__)

  Returns:
    `True` if successfully unregistered a listener.

  Since: v4.0
  """
  await_script_function("unregister_mouse_event_listener", ())


class ChatEventListener(EventRegistrationHandler):
  """Listener for chat message events.

  Only one `ChatEventListener` can be instantiated at a time within a job.

  Listener receives both incoming and outgoing chat messages.

  Inherits `register()` and `unregister()` methods from the base class,
  `EventRegistrationHandler`. These methods both return `bool` indicating
  whether the operation succeeded. Calling `register()` on a listener that's
  already registered returns `False`, and similarly for calling `unregister()`
  on a listener that's already unregistered.

  Implements context management so that it can be used with a `with` expression
  to automatically unregister the listener at the end of the block, e.g.

  ```
  messages = []
  with ChatEventListener() as listener:
    # Read next 3 messages from chat:
    for i in range(3):
      messages.append(listener.get())

  # listener no longer registered here...
  ```

  Update in v4.0:
    Addition of `register()`, `unregister()`, and context management via `with` expression.

  Since: v3.2
  """

  def __init__(self, register=True):
    """Creates a `ChatEventListener` to listen for chat messages.

    Args:
      register: if `True`, register the listener upon construction

    Update in v4.0:
      Added optional arg `register`.
    """
    super().__init__(
        register, register_chat_message_listener, unregister_chat_message_listener)

  def get(self, block: bool = True, timeout: float = None) -> str:
    """Gets the next chat event in the queue.

    Args:
      block: if `True`, block until an event fires
      timeout: timeout in seconds to wait for an event if `block` is `True`

    Returns:
      message from chat

    Raises:
      `queue.Empty` if `block` is `True` and `timeout` expires, or `block` is `False` and
      queue is empty.
    """
    return super().get(block, timeout)


def register_chat_message_listener(
    listener: Callable[[str], None], exception_handler: ExceptionHandler = None):
  """Registers a listener for receiving chat messages. One listener allowed per job.

  Listener receives both incoming and outgoing chat messages.

  For a more user-friendly API, use `ChatEventListener` instead.  (__internal__)

  Args:
    listener: callable that repeatedly accepts a string representing chat messages
    exception_handler: callable for handling an `Exception` thrown from Java (optional)

  Update in v3.2:
    Added optional arg `exception_handler`.

  Since: v2.0

  See also:
    `register_chat_message_interceptor()` for swallowing outgoing chat messages
  """
  send_script_function_request("register_chat_message_listener", (), listener, exception_handler)


def unregister_chat_message_listener():
  """Unregisters a chat message listener, if any, for the currently running job.

  For a more user-friendly API, use `ChatEventListener` instead.  (__internal__)

  Returns:
    `True` if successfully unregistered a listener.

  Since: v2.0
  """
  await_script_function("unregister_chat_message_listener", ())


class ChatMessageInterceptor(EventRegistrationHandler):
  """Interceptor of outgoing chat messages.

  Only one `ChatMessageInterceptor` can be registered per Minecraft instance.

  Intercepts outgoing chat messages and returns those intercepted messages from get().

  Inherits `register()` and `unregister()` methods from the base class,
  `EventRegistrationHandler`. These methods both return `bool` indicating
  whether the operation succeeded. Calling `register()` on an interceptor
  that's already registered returns `False`, and similarly for calling
  `unregister()` on an interceptor that's already unregistered.

  Implements context management so that it can be used with a `with` expression
  to automatically unregister the interceptor at the end of the block, e.g.

  ```
  messages = []
  with ChatMessageInterceptor() as interceptor:
    # Intercept next 3 messages from chat:
    for i in range(3):
      messages.append(interceptor.get())

  # interceptor no longer registered here...
  ```

  Since: v4.0
  """

  def __init__(self, register=True):
    """Creates a `ChatMessageInterceptor` to intercept chat messages.

    Args:
      register: if `True`, register the interceptor upon construction
    """
    super().__init__(
        register, register_chat_message_interceptor, unregister_chat_message_interceptor)

  def get(self, block: bool = True, timeout: float = None) -> str:
    """Gets the next intercepted chat message in the queue.

    Args:
      block: if `True`, block until an event fires
      timeout: timeout in seconds to wait for an event if `block` is `True`

    Returns:
      outgoing message intercepted from chat

    Raises:
      `queue.Empty` if `block` is `True` and `timeout` expires, or `block` is `False` and
      queue is empty.
    """
    return super().get(block, timeout)


def register_chat_message_interceptor(
    interceptor: Callable[[str], None], exception_handler: ExceptionHandler = None):
  """Registers an interceptor for swallowing chat messages.

  For a more user-friendly API, use `ChatMessageInterceptor` instead.  (__internal__)

  An interceptor swallows outgoing chat messages, typically for use in
  rewriting outgoing chat messages by calling minecraft.chat(str), e.g. to
  decorate or post-process outgoing messages automatically before they're sent
  to the server.  Only one interceptor is allowed at a time within a Minecraft
  instance.

  Args:
    interceptor: callable that repeatedly accepts a string representing chat messages
    exception_handler: callable for handling an `Exception` thrown from Java (optional)

  Since: v2.1

  See also:
    `register_chat_message_listener()` for non-destructive listening of chat messages
  """
  send_script_function_request(
      "register_chat_message_interceptor", (), interceptor, exception_handler)


def unregister_chat_message_interceptor():
  """Unregisters the chat message interceptor, if one is currently registered.

  For a more user-friendly API, use `ChatMessageInterceptor` instead.  (__internal__)

  Returns:
    `True` if successfully unregistered an interceptor.

  Since: v2.1
  """
  await_script_function("unregister_chat_message_interceptor", ())


def screen_name() -> str:
  """Gets the current GUI screen name, if there is one.

  Returns:
    Name of current screen (str) or `None` if no GUI screen is being displayed.

  Since: v3.2
  """
  return await_script_function("screen_name", ())


def container_get_items():
  """Gets all items in an open container (chest, furnace, etc. with slots).

  Returns:
    List of dictionaries of item data if a container's contents are displayed; `None` otherwise.

  Since: v4.0
  """
  return await_script_function("container_get_items", ())


def container_click_slot(slot: int) -> bool:
  """Simulates a left click on a slot in an open container, if any.

  Args:
    slot: slot number to click

  Returns:
    `True` upon success

  Since: v4.0
  """
  return await_script_function("container_click_slot", (slot,))


def player_look_at(x: float, y: float, z: float):
  """Rotates the camera to look at a position.

  Args:
    x: x position
    y: y position
    z: z position

  Since: v4.0
  """
  await_script_function("player_look_at", (x, y, z))


BlockPos = Tuple[int, int, int]
"""Tuple representing `(x: int, y: int, z: int)` position in block space."""


Rotation = Tuple[int, int, int, int, int, int, int, int, int]
"""Tuple of 9 `int` values representing a flattened, row-major 3x3 rotation matrix."""


class Rotations:
  """Common rotations for use with `BlockPack` and `BlockPacker` methods.

  Since: v3.0
  """

  IDENTITY: Rotation = (1, 0, 0, 0, 1, 0, 0, 0, 1)
  """Effectively no rotation."""

  X_90: Rotation = (1, 0, 0, 0, 0, 1, 0, -1, 0)
  """Rotate 90 degrees about the x axis."""

  X_180: Rotation = (1, 0, 0, 0, -1, 0, 0, 0, -1)
  """Rotate 180 degrees about the x axis."""

  X_270: Rotation = (1, 0, 0, 0, 0, -1, 0, 1, 0)
  """Rotate 270 degrees about the x axis."""

  Y_90: Rotation = (0, 0, 1, 0, 1, 0, -1, 0, 0)
  """Rotate 90 degrees about the y axis."""

  Y_180: Rotation = (-1, 0, 0, 0, 1, 0, 0, 0, -1)
  """Rotate 180 degrees about the y axis."""

  Y_270: Rotation = (0, 0, -1, 0, 1, 0, 1, 0, 0)
  """Rotate 270 degrees about the y axis."""

  Z_90: Rotation = (0, 1, 0, -1, 0, 0, 0, 0, 1)
  """Rotate 90 degrees about the z axis."""

  Z_180: Rotation = (-1, 0, 0, 0, -1, 0, 0, 0, 1)
  """Rotate 180 degrees about the z axis."""

  Z_270: Rotation = (0, -1, 0, 1, 0, 0, 0, 0, 1)
  """Rotate 270 degrees about the z axis."""

  INVERT_X: Rotation = (-1, 0, 0, 0, 1, 0, 0, 0, 1)
  """Invert the x coordinate (multiply by -1)."""

  INVERT_Y: Rotation = (1, 0, 0, 0, -1, 0, 0, 0, 1)
  """Invert the y coordinate (multiply by -1)."""

  INVERT_Z: Rotation = (1, 0, 0, 0, 1, 0, 0, 0, -1)
  """Invert the z coordinate (multiply by -1)."""


# TODO(maxuser): Move this into Rotations class and rename to compose(...).
def combine_rotations(rot1: Rotation, rot2: Rotation, /) -> Rotation:
  """Combines two rotation matrices into a single rotation matrix.

  Since: v3.0
  """
  return (
      rot1[0] * rot2[0] + rot1[1] * rot2[3] + rot1[2] * rot2[6],
      rot1[0] * rot2[1] + rot1[1] * rot2[4] + rot1[2] * rot2[7],
      rot1[0] * rot2[2] + rot1[1] * rot2[5] + rot1[2] * rot2[8],
      rot1[3] * rot2[0] + rot1[4] * rot2[3] + rot1[5] * rot2[6],
      rot1[3] * rot2[1] + rot1[4] * rot2[4] + rot1[5] * rot2[7],
      rot1[3] * rot2[2] + rot1[4] * rot2[5] + rot1[5] * rot2[8],
      rot1[6] * rot2[0] + rot1[7] * rot2[3] + rot1[8] * rot2[6],
      rot1[6] * rot2[1] + rot1[7] * rot2[4] + rot1[8] * rot2[7],
      rot1[6] * rot2[2] + rot1[7] * rot2[5] + rot1[8] * rot2[8])


def blockpack_read_world(
    pos1: BlockPos, pos2: BlockPos,
    rotation: Rotation = None, offset: BlockPos = None,
    comments: Dict[str, str] = {}, safety_limit: bool = True) -> int:
  """Creates a blockpack from blocks in the world within a rectangular volume.

  For a more user-friendly API, use the `BlockPack` class instead. (__internal__)

  Args:
    pos1, pos2: opposing corners of a rectangular volume from which to read world blocks
    rotation: rotation matrix to apply to block coordinates read from world
    offset: offset to apply to block coordiantes (applied after rotation)
    comments: key, value pairs to include in the new blockpack
    safety_limit: if `True`, fail if requested volume spans more than 1600 chunks

  Returns:
    an int id associated with a new blockpack upon success, `None` otherwise

  Since: v3.0
  """
  return await_script_function(
      "blockpack_read_world", (pos1, pos2, rotation, offset, comments, safety_limit))


def blockpack_read_file(filename: str) -> int:
  """Reads a blockpack from a file.

  For a more user-friendly API, use the `BlockPack` class instead. (__internal__)

  Args:
    filename: name of file to read; relative to Minecraft dir unless it's an absolute path
        (".zip" is automatically appended to filename if it does not end with that extension)

  Returns:
    an int id associated with a blockpack upon success

  Since: v3.0
  """
  return await_script_function("blockpack_read_file", (filename,))


def blockpack_import_data(base64_data: str) -> int:
  """Creates a blockpack from base64-encoded serialized blockpack data.

  For a more user-friendly API, use the `BlockPack` class instead. (__internal__)

  Args:
    base64_data: base64-encoded string containing serialization of blockpack data.

  Returns:
    an int id associated with a blockpack upon success, `None` otherwise

  Since: v3.0
  """
  return await_script_function("blockpack_import_data", (base64_data,))


def blockpack_block_bounds(blockpack_id: int) -> (BlockPos, BlockPos):
  """Returns bounding coordinates of blocks in the blockpack associated with blockpack_id.

  For a more user-friendly API, use the `BlockPack` class instead. (__internal__)

  Since: v3.0
  """
  return await_script_function("blockpack_block_bounds", (blockpack_id,))


def blockpack_comments(blockpack_id: int) -> Dict[str, str]:
  """Returns comments stored in the blockpack associated with blockpack_id.

  For a more user-friendly API, use the `BlockPack` class instead. (__internal__)

  Since: v3.0
  """
  return await_script_function("blockpack_comments", (blockpack_id,))


def blockpack_write_world(
    blockpack_id: int, rotation: Rotation = None, offset: BlockPos = None) -> bool:
  """Writes blocks from a blockpack into the current world. Requires setblock and fill commands.

  For a more user-friendly API, use the `BlockPack` class instead. (__internal__)

  Args:
    blockpack_id: id of a currently loaded blockpack
    rotation: rotation matrix to apply to block coordinates before writing to world
    offset: offset to apply to block coordiantes (applied after rotation)

  Returns:
    `True` upon success

  Since: v3.0
  """
  return await_script_function("blockpack_write_world", (blockpack_id, rotation, offset))


def blockpack_write_file(blockpack_id: int, filename: str) -> bool:
  """Writes a blockpack to a file.

  For a more user-friendly API, use the `BlockPack` class instead. (__internal__)

  Args:
    blockpack_id: id of a currently loaded blockpack
    filename: name of file to write; relative to Minecraft dir unless it's an absolute path
        (".zip" is automatically appended to filename if it does not end with that extension)

  Returns:
    `True` upon success

  Since: v3.0
  """
  return await_script_function("blockpack_write_file", (blockpack_id, filename))


def blockpack_export_data(blockpack_id: int) -> str:
  """Serializes a blockpack into a base64-encoded string.

  For a more user-friendly API, use the `BlockPack` class instead. (__internal__)

  Args:
    blockpack_id: id of a currently loaded blockpack

  Returns:
    a base64-encoded string containing a serialized blockpack

  Since: v3.0
  """
  return await_script_function("blockpack_export_data", (blockpack_id,))


def blockpack_delete(blockpack_id: int) -> bool:
  """Frees a currently loaded blockpack to be garbage collected.

  For a more user-friendly API, use the `BlockPack` class instead. (__internal__)

  Args:
    blockpack_id: id of a currently loaded blockpack

  Returns:
    `True` upon success

  Since: v3.0
  """
  return await_script_function("blockpack_delete", (blockpack_id,))


def blockpacker_create() -> int:
  """Creates a new, empty blockpacker.

  For a more user-friendly API, use the `BlockPacker` class instead. (__internal__)

  Returns:
    an int id associated with a new blockpacker

  Since: v3.0
  """
  return await_script_function("blockpacker_create", ())


def blockpacker_add_blocks(
    blockpacker_id: int, offset: BlockPos,
    base64_setblocks: str, base64_fills: str, blocks: List[str]) -> bool:
  """Adds blocks from setblocks and fills arrays to a currently loaded blockpacker.

  For a more user-friendly API, use the `BlockPacker` class instead. (__internal__)

  Args:
    blockpacker_id: id of a currently loaded blockpacker
    offset: offset from 16-bit positions in `base64_setblocks` and `base64_fills`
    base64_setblocks: base64-encoded array of 16-bit signed ints where every 4 values are:
      x, y, z relative to `offset` and index into `blocks` list
    base64_fills: base64-encoded array of 16-bit signed ints where every 7 values are:
      x1, y1, z1, x2, y2, z2 relative to `offset` and index into `blocks` list
    blocks: types of blocks referenced from `base64_setblocks` and `base64_fills` arrays

  Returns:
    `True` upon success

  Since: v3.1
  """
  return await_script_function(
      "blockpacker_add_blocks", (blockpacker_id, offset, base64_setblocks, base64_fills, blocks))


def blockpacker_add_blockpack(
    blockpacker_id: int, blockpack_id: int,
    rotation: Rotation = None, offset: BlockPos = None) -> bool:
  """Adds the blocks within a currently loaded blockpack into a blockpacker.

  For a more user-friendly API, use the `BlockPacker` class instead. (__internal__)

  Args:
    blockpacker_id: id of a blockpacker to receive blocks
    blockpack_id: id of a blockpack from which to copy blocks
    rotation: rotation matrix to apply to block coordinates before adding to blockpacker
    offset: offset to apply to block coordiantes (applied after rotation)

  Returns:
    `True` upon success

  Since: v3.0
  """
  return await_script_function(
      "blockpacker_add_blockpack", (blockpacker_id, blockpack_id, rotation, offset))


def blockpacker_pack(blockpacker_id: int, comments: Dict[str, str]) -> int:
  """Packs blocks within a blockpacker into a new blockpack.

  For a more user-friendly API, use the `BlockPacker` class instead. (__internal__)

  Args:
    blockpacker_id: id of a currently loaded blockpacker
    comments: key, value pairs to include in the new blockpack

  Returns:
    int id for a new blockpack containing a snapshot of blocks from the blockpacker

  Since: v3.0
  """
  return await_script_function("blockpacker_pack", (blockpacker_id, comments))


def blockpacker_delete(blockpacker_id: int) -> bool:
  """Frees a currently loaded blockpacker to be garbage collected.

  For a more user-friendly API, use the `BlockPacker` class instead. (__internal__)

  Args:
    blockpacker_id: id of a currently loaded blockpacker

  Returns:
    `True` upon success

  Since: v3.0
  """
  return await_script_function("blockpacker_delete", (blockpacker_id,))


class BlockPack:
  """BlockPack is an immutable and serializable collection of blocks.

  A blockpack can be read from or written to worlds, files, and serialized
  bytes. Although blockpacks are immutable and preserve position and
  orientation of blocks, they can be rotated and offset when read from or
  written to worlds.

  For a mutable collection of blocks, see `BlockPacker`.

  Since: v3.0
  """

  def __init__(self, java_generated_id: int):
    """Do not call the constructor directly. Use factory classmethods instead.

    (__internal__)
    """
    self._id = java_generated_id

  @classmethod
  def read_world(
      cls,
      pos1: BlockPos, pos2: BlockPos, *,
      rotation: Rotation = None, offset: BlockPos = None,
      comments: Dict[str, str] = {}, safety_limit: bool = True) -> 'BlockPack':
    """Creates a blockpack from blocks in the world within a rectangular volume.

    Args:
      pos1, pos2: opposing corners of a rectangular volume from which to read world blocks
      rotation: rotation matrix to apply to block coordinates read from world
      offset: offset to apply to block coordiantes (applied after rotation)
      comments: key, value pairs to include in the new blockpack
      safety_limit: if `True`, fail if requested volume spans more than 1600 chunks

    Returns:
      a new BlockPack containing blocks read from the world
    """
    blockpack_id = blockpack_read_world(pos1, pos2, rotation, offset, comments, safety_limit)
    return BlockPack(blockpack_id)

  @classmethod
  def read_file(cls, filename: str, *, relative_to_cwd=False) -> 'BlockPack':
    """Reads a blockpack from a file.

    Args:
      filename: name of file relative to minescript/blockpacks dir unless it's an absolute path
        (".zip" is automatically appended to filename if it does not end with that extension)
      relative_to_cwd: if `True`, relative filename is taken to be relative to Minecraft dir

    Returns:
      a new BlockPack containing blocks read from the file
    """
    if not os.path.isabs(filename) and not relative_to_cwd:
      filename = os.path.join("minescript", "blockpacks", filename)
    return BlockPack(blockpack_read_file(filename))

  @classmethod
  def import_data(cls, base64_data: str) -> 'BlockPack':
    """Creates a blockpack from base64-encoded serialized blockpack data.

    Args:
      base64_data: base64-encoded string containing serialization of blockpack data.

    Returns:
      a new BlockPack containing blocks read from the base64-encoded data
    """
    return BlockPack(blockpack_import_data(base64_data))

  def block_bounds(self) -> (BlockPos, BlockPos):
    """Returns min and max bounding coordinates of blocks in this BlockPack."""
    return blockpack_block_bounds(self._id)

  def comments(self) -> Dict[str, str]:
    """Returns comments stored in this BlockPack."""
    return blockpack_comments(self._id)

  def write_world(self, *, rotation: Rotation = None, offset: BlockPos = None):
    """Writes blocks from this BlockPack into the current world. Requires setblock, fill commands.

    Args:
      rotation: rotation matrix to apply to block coordinates before writing to world
      offset: offset to apply to block coordiantes (applied after rotation)
    """
    blockpack_write_world(self._id, rotation, offset)

  def write_file(self, filename: str, *, relative_to_cwd=False):
    """Writes this BlockPack to a file.

    Args:
      filename: name of file relative to minescript/blockpacks dir unless it's an absolute path
        (".zip" is automatically appended to filename if it does not end with that extension)
      relative_to_cwd: if `True`, relative filename is taken to be relative to Minecraft dir
    """
    if not os.path.isabs(filename) and not relative_to_cwd:
      filename = os.path.join("minescript", "blockpacks", filename)
    blockpack_write_file(self._id, filename)

  def export_data(self) -> str:
    """Serializes this BlockPack into a base64-encoded string.

    Returns:
      a base64-encoded string containing this blockpack's data
    """
    return blockpack_export_data(self._id)

  def __del__(self):
    """Frees this BlockPack to be garbage collected."""
    blockpack_delete(self._id)


class BlockPackerException(Exception):
  pass


def _pos_subtract(pos1: BlockPos, pos2: BlockPos) -> BlockPos:
  """Returns pos1 minus pos2."""
  return (pos1[0] - pos2[0], pos1[1] - pos2[1], pos1[2] - pos2[2])


_SETBLOCKS_ARRAY_THRESHOLD = 4000
_FILLS_ARRAY_THRESHOLD = 7000
_BLOCKS_DICT_THRESHOLD = 1000

class BlockPacker:
  """BlockPacker is a mutable collection of blocks.

  Blocks can be added to a blockpacker by calling `setblock(...)`, `fill(...)`,
  and/or `add_blockpack(...)`.  To serialize blocks or write them to a world, a
  blockpacker can be "packed" by calling pack() to create a compact snapshot of
  the blocks contained in the blockpacker in the form of a new BlockPack. A
  blockpacker continues to store the same blocks it had before being packed,
  and more blocks can be added thereafter.

  For a collection of blocks that is immutable and serializable, see `BlockPack`.

  Since: v3.0
  """

  def __init__(self):
    """Creates a new, empty blockpacker."""

    self._id = blockpacker_create()
    self.offset = None # offset for 16-bit positions recorded in setblocks and fills
    self.setblocks = array("h")
    self.fills = array("h")
    self.blocks: Dict[str, int] = dict()

  def _get_block_id(self, block_type: str) -> int:
    return self.blocks.setdefault(block_type, len(self.blocks))

  def setblock(self, pos: BlockPos, block_type: str):
    """Sets a block within this BlockPacker.

    Args:
      pos: position of a block to set
      block_type: block descriptor to set

    Raises:
      `BlockPackerException` if blockpacker operation fails
    """
    if self.offset is None:
      self.offset = pos

    relative_pos = _pos_subtract(pos, self.offset)
    if max(relative_pos) > 32767 or min(relative_pos) < -32768:
      raise BlockPackerException(
          f"Blocks within a Python-generated BlockPacker cannot span more than 32,767 blocks: "
          f"{self.offset} -> {pos}")

    self.setblocks.extend(relative_pos)
    self.setblocks.append(self._get_block_id(block_type))

    if (len(self.setblocks) > _SETBLOCKS_ARRAY_THRESHOLD or
        len(self.blocks) > _BLOCKS_DICT_THRESHOLD):
      self._flush_blocks()

  def fill(self, pos1: BlockPos, pos2: BlockPos, block_type: str):
    """Fills blocks within this BlockPacker.

    Args:
      pos1, pos2: coordinates of opposing corners of a rectangular volume to fill
      block_type: block descriptor to fill

    Raises:
      `BlockPackerException` if blockpacker operation fails
    """
    if self.offset is None:
      self.offset = pos1

    relative_pos1 = _pos_subtract(pos1, self.offset)
    if max(relative_pos1) > 32767 or min(relative_pos1) < -32768:
      raise BlockPackerException(
          f"Blocks within a Python-generated BlockPacker cannot span more than 32,767 blocks: "
          f"{self.offset} -> {pos1}")

    relative_pos2 = _pos_subtract(pos2, self.offset)
    if max(relative_pos2) > 32767 or min(relative_pos2) < -32768:
      raise BlockPackerException(
          f"Blocks within a Python-generated BlockPacker cannot span more than 32,767 blocks: "
          f"{self.offset} -> {pos2}")

    self.fills.extend(relative_pos1)
    self.fills.extend(relative_pos2)
    self.fills.append(self._get_block_id(block_type))

    if (len(self.fills) > _FILLS_ARRAY_THRESHOLD or
        len(self.blocks) > _BLOCKS_DICT_THRESHOLD):
      self._flush_blocks()

  def _flush_blocks(self):
    if sys.byteorder != "big":
      # Swap to network (big-endian) byte order.
      self.setblocks.byteswap()
      self.fills.byteswap()

    blockpacker_add_blocks(
        self._id, self.offset,
        base64.b64encode(self.setblocks.tobytes()).decode("utf-8"),
        base64.b64encode(self.fills.tobytes()).decode("utf-8"),
        list(self.blocks.keys()))

    self.offset = None
    self.setblocks = array("h")
    self.fills = array("h")
    self.blocks = dict()

  def add_blockpack(
      self, blockpack: BlockPack, *, rotation: Rotation = None, offset: BlockPos = None):
    """Adds the blocks within a BlockPack into this BlockPacker.

    Args:
      blockpack: BlockPack from which to copy blocks
      rotation: rotation matrix to apply to block coordinates before adding to blockpacker
      offset: offset to apply to block coordiantes (applied after rotation)
    """
    blockpacker_add_blockpack(self._id, blockpack._id, rotation, offset)

  def pack(self, *, comments: Dict[str, str] = {}) -> BlockPack:
    """Packs blocks within this BlockPacker into a new BlockPack.

    Args:
      comments: key, value pairs to include in the new BlockPack

    Returns:
      a new BlockPack containing a snapshot of blocks from this BlockPacker
    """
    self._flush_blocks()
    return BlockPack(blockpacker_pack(self._id, comments))

  def __del__(self):
    """Frees this BlockPacker to be garbage collected."""
    blockpacker_delete(self._id)

