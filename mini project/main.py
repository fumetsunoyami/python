import pygame
import sys
import random
from moviepy.editor import VideoFileClip

pygame.init()

# khu vuc tao man hinh nen 
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
'SCREEN_ASPECT_RATIO = 16 / 9'



WHITE = (255, 255, 255)


background = pygame.image.load("D:\\CTK45B_2115230_NguyenVietLinh_B!\\mini project\\a.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
'background_height = int(WIDTH / SCREEN_ASPECT_RATIO)'

#ending 
ending = VideoFileClip("D:\\CTK45B_2115230_NguyenVietLinh_B!\\mini project\\ending.mp4")




#tao doi tuong may bay

plane = pygame.image.load("D:\\CTK45B_2115230_NguyenVietLinh_B!\\mini project\\plane.png")
plane = pygame.transform.scale(plane, (150, 75))
plane_rect = plane.get_rect()
plane_rect.center = (300, HEIGHT // 2)

#vat the 
obstacle_image = pygame.image.load("D:\\CTK45B_2115230_NguyenVietLinh_B!\\mini project\\tower.png")
obstacle_image = pygame.transform.scale(obstacle_image, (165, 870))
obstacle_rect = obstacle_image.get_rect()
obstacle_rect.x = WIDTH 
obstacle_rect.y = random.randint(100, HEIGHT - 100)
obstacles = []
#diem so
score = 0
scored_obstacles = []
font = pygame.font.Font(None, 36)
score_text = font.render(f"Saved lives: {score}k", True, (255, 255, 255))
score_rect = score_text.get_rect()
score_rect.topright = (WIDTH - 100, 100)




#thong so
obstacle_speed = 5
background_speed = 0.3
background_x = 0
fall_speed = 5
jump_speed = 12
rotation_angle = 0
rotation_flyup = 10
rotation_flydown = -15
gap_height = 520
obstacle_spawn = 300  # 2 giây
#hitbox
plane_mask = pygame.mask.from_surface(plane)
obstacle_mask = pygame.mask.from_surface(obstacle_image)


#tao vat the 
def create_obstacle():
    obstacle_width = 100
    obstacle_height = random.randint(100, HEIGHT - gap_height - 100)
    bottom_obstacle_rect = pygame.Rect(WIDTH, obstacle_height + gap_height, obstacle_width, HEIGHT - obstacle_height - gap_height)
    top_obstacle_rect = pygame.Rect(WIDTH, obstacle_height - gap_height, obstacle_width, obstacle_height)
    obstacles.extend([top_obstacle_rect, bottom_obstacle_rect])
    


    
#kiem tra va cham
def check_collision(plane_rect, obstacles):
    for obstacle_rect in obstacles:
        obstacle_mask_offset = (obstacle_rect.x - plane_rect.x, obstacle_rect.y - plane_rect.y)
        collision = plane_mask.overlap(obstacle_mask, obstacle_mask_offset)
        if collision:
            return True
    return False
#man hinh thong bao (chưa sử dụng)
'''def show_message_screen():
    screen.fill(WHITE)
    screen.blit(background, (0, 0))

    
    play_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100)
    pygame.draw.rect(screen, (0, 128, 255), play_button)

    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(score_text, score_rect)

    
    message_text = font.render("press SPACE to play", True, (255, 255, 255))
    message_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(message_text, message_rect)

    pygame.display.flip()'''
#main 
def main():
    clock = pygame.time.Clock()
    
    running = True
   

    while running:
        global background_speed, background_x, rotation_angle, score, score_text 
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
           
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            plane_rect.y -=  jump_speed
            rotation_angle = rotation_flyup
        else:   
            plane_rect.y += fall_speed  
            rotation_angle = rotation_flydown
        
        
        
         
      
        
        
        
        
        background_x -= background_speed
        
    
        if background_x <= -WIDTH:
            background_x = 0

     
       

      
        screen.fill(WHITE)
        screen.blit(background, (background_x, 0))
        screen.blit(background, (background_x + WIDTH, 0))
        
        rotated_plane = pygame.transform.rotate(plane, rotation_angle)  
        rotated_plane_rect = rotated_plane.get_rect(center=plane_rect.center)

        screen.blit(rotated_plane, rotated_plane_rect)
        if len(obstacles) == 0 or obstacles[-1].x <= WIDTH - obstacle_spawn:
            create_obstacle()
        for obstacle_rect in obstacles:
            obstacle_rect.x -= obstacle_speed  
            screen.blit(obstacle_image, obstacle_rect)
            
        if plane_rect.bottom > HEIGHT:
            plane_rect.bottom = HEIGHT     
            
        if plane_rect.bottom < 0:
            plane_rect.bottom = 0 
            
        collision = check_collision(plane_rect, obstacles)
        if collision or plane_rect.bottom == HEIGHT:
            
            
            running = False
        else:
            for obstacle_rect in obstacles:
                if obstacle_rect.x + obstacle_rect.width < plane_rect.x and obstacle_rect not in scored_obstacles:
                    score += 1.5
                    scored_obstacles.append(obstacle_rect)
        score_text = font.render(f"Saved lives: {score}k", True, (255, 255, 255))
       
   
        screen.blit(score_text, score_rect)

        pygame.display.flip()
        clock.tick(60)
        
    if running == False: 
        ending.preview()
        

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
