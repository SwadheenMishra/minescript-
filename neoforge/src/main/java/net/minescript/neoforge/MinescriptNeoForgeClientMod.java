// SPDX-FileCopyrightText: © 2022-2024 Greg Christiana <maxuser@minescript.net>
// SPDX-License-Identifier: GPL-3.0-only

package net.minescript.neoforge;

import static net.minescript.common.Minescript.ENTER_KEY;
import static net.minescript.common.Minescript.config;

import net.minecraft.client.Minecraft;
import net.minecraft.client.multiplayer.ClientLevel;
import net.minescript.common.Minescript;
import net.neoforged.api.distmarker.Dist;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.LogicalSide;
import net.neoforged.fml.common.Mod;
import net.neoforged.fml.event.lifecycle.FMLClientSetupEvent;
import net.neoforged.neoforge.client.event.InputEvent;
import net.neoforged.neoforge.client.event.ScreenEvent;
import net.neoforged.neoforge.event.TickEvent;
import net.neoforged.neoforge.event.level.ChunkEvent;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class MinescriptNeoForgeClientMod {
  private static final Logger LOGGER = LogManager.getLogger();

  public MinescriptNeoForgeClientMod() {}

  @Mod.EventBusSubscriber(
      modid = Constants.MODID,
      bus = Mod.EventBusSubscriber.Bus.MOD,
      value = Dist.CLIENT)
  public static class ClientModEvents {
    @SubscribeEvent
    public static void onClientSetup(FMLClientSetupEvent event) {
      LOGGER.info("(minescript) Minescript mod starting...");
      Minescript.init(new NeoForgePlatform());
    }
  }

  @Mod.EventBusSubscriber(Dist.CLIENT)
  public static class ClientEvents {
    @SubscribeEvent
    public static void onKeyboardKeyPressedEvent(ScreenEvent.KeyPressed.Pre event) {
      if (Minescript.onKeyboardKeyPressed(event.getScreen(), event.getKeyCode())) {
        event.setCanceled(true);
      }
    }

    @SubscribeEvent
    public static void onKeyInputEvent(InputEvent.Key event) {
      var key = event.getKey();
      var scanCode = event.getScanCode();
      var action = event.getAction();
      var modifiers = event.getModifiers();
      Minescript.onKeyboardEvent(key, scanCode, action, modifiers);
      var screen = Minecraft.getInstance().screen;
      if (screen == null) {
        Minescript.onKeyInput(key);
      } else if ((key == ENTER_KEY || key == config.secondaryEnterKeyCode())
          && action == Constants.KEY_ACTION_DOWN
          && Minescript.onKeyboardKeyPressed(screen, key)) {
        // TODO(maxuser): InputEvent.Key isn't cancellable with NeoForge.
        // event.setCanceled(true);
      }
    }

    @SubscribeEvent
    public static void onChunkLoadEvent(ChunkEvent.Load event) {
      if (event.getLevel() instanceof ClientLevel) {
        Minescript.onChunkLoad(event.getLevel(), event.getChunk());
      }
    }

    @SubscribeEvent
    public static void onChunkUnloadEvent(ChunkEvent.Unload event) {
      if (event.getLevel() instanceof ClientLevel) {
        Minescript.onChunkUnload(event.getLevel(), event.getChunk());
      }
    }

    @SubscribeEvent
    public static void onWorldTick(TickEvent.LevelTickEvent event) {
      if (event.side == LogicalSide.CLIENT && event.phase == TickEvent.Phase.START) {
        Minescript.onClientWorldTick();
      }
    }
  }
}
