import pygame
import time
import os
 
# 初始化设置字体
pygame.font.init()
font_path = os.path.join(os.path.dirname(r"D:\python\Practice\Bold.ttf"), 'Bold.ttf')
 
class Solider:
    def __init__(self, screen,x_position,y_position):
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.text_surface = self.font.render('~^$^~',True,(255,255,255))
        self.X_position = x_position
        self.Y_position = y_position
    def draw(self):
        self.screen.blit(self.text_surface,(self.X_position,self.Y_position))
 
class Leader:
    def __init__(self,screen,x_position,y_position):
        self.screen = screen
        self.font = pygame.font.Font(font_path, 30)
        self.text_surface = self.font.render('少帅',True,(255,255,255))
        self.X_position = x_position
        self.Y_position = y_position
        self.visible = False
 
    def draw(self):
        if self.visible:
            self.screen.blit(self.text_surface,(self.X_position,self.Y_position))
 
    def move(self):
        if self.Y_position < 450 and self.visible:
            self.Y_position += 3
 
class Plane:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
 
        # 定义飞机的框架
        self.iplanes = [
            "  ~o|                  ",
            "  ~>=======>>  ",
            "  ~o|                  "
        ]
 
        # render将一段文字转换成为一个surface对象
        self.text_surfaces = [self.font.render(line, True, (255, 255, 255)) for line in self.iplanes]
        self.total_height = sum([text.get_height() for text in self.text_surfaces])
        self.X_position = 20
        self.Y_position = 40
 
    # 绘制飞机
    def draw(self):
        # 定义临时变量跟踪当前Y轴位置
        current_y = self.Y_position
        for surface in self.text_surfaces:
            self.screen.blit(surface, (self.X_position, current_y))
            current_y += surface.get_height()
 
    # 实现飞机移动
    def move(self,distance):
        self.X_position += distance
 
    def get_leftmost_position(self):
 
        # 获得字符串中的最大宽度值作为整体宽度
        max_width = max([text.get_width() for text in self.text_surfaces])
        leftmost_position = self.X_position - max_width // 2      # 计算飞机左侧位置
        return leftmost_position                                 # 返回左侧位置
 
class Shaoshuai:
    def __init__(self, screen):
        self.screen = screen
        self.plane = Plane(screen)
        self.stop_position = 300
        self.solider1 = Solider(screen,self.stop_position-30,450)
        self.solider2 = Solider(screen,self.stop_position+200,450)
        self.leader = Leader(screen,self.stop_position + 80,40)
        self.clock = pygame.time.Clock()
        self.pause_time = None
        self.screen_width,self.screen_height = screen.get_size()
        self.is_destroyed = False    #设置是否被摧毁的符号
 
 
    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.screen.fill((0, 0, 0))  # 清屏
            self.solider1.draw()  # 显示卫兵
            self.solider2.draw()
            self.leader.draw()        # 显示少帅
 
            #如果到达指定暂停位置，生成暂停条件
            if self.plane.X_position == self.stop_position and self.pause_time is None :
                self.pause_time = time.time()
                self.leader.visible = True
 
            # 如果达到解除暂停条件的时间，解除暂停
            if self.pause_time is not None and time.time() - self.pause_time > 2:
                self.pause_time = None
 
            #判断飞机是否飞出屏幕
            if self.plane.get_leftmost_position() > self.screen_width :
 
                # print输出信息确保此段代码执行，更改is_destroyed的标识符执行飞机被摧毁的操作
                # print("飞机被摧毁！")
                self.is_destroyed = True
 
            #判断暂停，以及是否飞出屏幕
            if self.pause_time is None:
                if not self.is_destroyed:
                    self.plane.move(10)  # 实现飞机移动
                    self.plane.draw()  # 显示飞机
 
                else:
                    pass
            else:
                self.plane.draw()      #只显示飞机框架，不实现移动
            self.leader.move()        # 实现少帅的移动
 
            pygame.display.flip()  # 更新屏幕
            self.clock.tick(30)  # 控制帧率
 
 
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('少帅')
    shaoshuai = Shaoshuai(screen)
    shaoshuai.main()