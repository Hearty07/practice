#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys

pygame.init()

# 创建一个窗口
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("鼠标滚轮控制音量大小")

# 加载音乐
pygame.mixer.music.load("bgm.mp3")

# 播放音乐
pygame.mixer.music.play(-1)

# 设置音量
pygame.mixer.music.set_volume(0.2)

while True:
    # 遍历所有事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 如果事件类型是滚轮事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 改变音量
            if event.button == 4:
                # 滚轮向上滚动，音量增加
                pygame.mixer.music.set_volume(min(1, pygame.mixer.music.get_volume()+0.1))
            elif event.button == 5:
                # 滚轮向下滚动，音量减小
                pygame.mixer.music.set_volume(max(0, pygame.mixer.music.get_volume()-0.1))

pygame.quit()