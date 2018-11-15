import pygame
import random
import webbrowser
import sys
pygame.init()
pygame.mixer.init()
try:
	pygame.mixer.music.load('music.wav')
except:
	class MUSIC:
		def set_volume(x):
			pass
		def get_pos():
			return None
		def play():
			pass
	pygame.mixer.music = MUSIC
	del MUSIC
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play()
display = pygame.display.set_mode((800,600))
pygame.display.set_caption('noisy rect')
try:
	pygame.display.set_icon(pygame.image.load('icon.ico'))
except:
	pass
try:
	font = pygame.font.SysFont('Lovelo',25)
except:
	sys.exit()
done = False
start_menu = True
apnd_num = 3
ballmap = [-25,-25]
right=True
down=True
def noisyball():
	global display,ballmap,right,down
	pygame.draw.circle(display, [255,0,255], ballmap, 25)
	if ballmap[0] < 775 and right:
		ballmap[0] += apnd_num
		if ballmap[0] >= 775:
			right = not right
	else:
		ballmap[0] -= apnd_num
		if ballmap[0] <= 25:
			right = not right
	if ballmap[1] < 575 and down:
		ballmap[1] += apnd_num
		if ballmap[1] >= 575:
			down = not down
	else:
		ballmap[1] -= apnd_num
		if ballmap[1] <= 25:
			down = not down

n2map = [25,25]
def noisy2():
	global display,n2map
	n2map = [n2map[0]+random.choice([-1*apnd_num,0,apnd_num]),n2map[1]+random.choice([-1*apnd_num,0,apnd_num])]
	if n2map[0] < 25:
		n2map[0] = 25
	if n2map[0] > 775:
		n2map[0] = 775
	if n2map[1] < 25:
		n2map[1] = 25
	if n2map[1] > 575:
		n2map[1] = 575
	pygame.draw.circle(display, [255,0,255], n2map, 25)

n3map = [25,25]
n3up = False
n3down = True
n3right = False
n3left = False
def noisy3():
	global display,n3map,n3up,n3right,n3down,n3left
	if n3down:
		n3map[1] += apnd_num
		if n3map[1] >= 575:
			n3down = not n3down
			n3right = not n3right
	elif n3right:
		n3map[0] += apnd_num
		if n3map[0] >= 775:
			n3right = not n3right
			n3up = not n3up
	elif n3up:
		n3map[1] -= apnd_num
		if n3map[1] <= 25:
			n3up = not n3up
			n3left = not n3left
	elif n3left:
		n3map[0] -= apnd_num
		if n3map[0] <= 25:
			n3left = not n3left
			n3down = not n3down
	pygame.draw.circle(display, [255,0,255], n3map, 25)
mball_pos = [350,500]
mball_rad = 40
adding = True
jump = False
show_help_on_start_game = True
helpfont = pygame.font.SysFont('Lovelo',20)
bad_rects = [
	[0,random.randint(0,550)],
	[-50,random.randint(0,550)],
	[-100,random.randint(0,550)],
	[-150,random.randint(0,550)],
	[-200,random.randint(0,550)],
	[-250,random.randint(0,550)],
	[-300,random.randint(0,550)],
	[-350,random.randint(0,550)]
]
my_score = 0
def badrects():
	global bad_rects,my_score
	wingame()
	for x in range(len(bad_rects)):
		if bad_rects[x][0] >= 875:
			bad_rects[x][0] = 0
			bad_rects[x][1] = random.randint(0,575)
		pygame.draw.rect(display, [0,0,255], bad_rects[x]+[25,25])
	for x in range(len(bad_rects)):
		bad_rects[x][0] += 4
	my_score += .005
def my_or(a,b):
	if not a and not b: 
		return True
	return False
def wingame():
	global bad_rects,mball_pos,lose_mode,my_score
	notchng = True
	for x in range(len(bad_rects)):
		if my_or(
			set(
				range(
					mball_pos[0],mball_pos[0] + 81
				)
			).isdisjoint(
				range(
					bad_rects[x][0],bad_rects[x][0] + 26
				)
			)
			,
			set(
				range(
					mball_pos[1],mball_pos[1] + 81
				)
			).isdisjoint(
				range(
					bad_rects[x][1],bad_rects[x][1] + 26
				)
			)
		):
			lose_mode = True
			notchng = False
			break
	if notchng:
		lose_mode = False
losefont = pygame.font.SysFont('Lovelo',37)
lose_bgcolor = [0,0,0]
def losescr():
	global my_score,lose_bgcolor
	display.fill(lose_bgcolor)
	pygame.draw.rect(display,[0,63,0],[150,250,500,50])
	display.blit(losefont.render("oops , your rect killed!",True,[0,75,75]),[150,258])
	display.blit(losefont.render("your rect score: "+str(int(my_score)),True,[0,75,75]),[150,308])
	if lose_bgcolor[0] < 127:
		lose_bgcolor[0] += 2
def resetgame():
	global lose_mode,bad_rects,mball_pos,my_score,lose_bgcolor
	bad_rects = [
	[0,random.randint(0,550)],
	[-50,random.randint(0,550)],
	[-100,random.randint(0,550)],
	[-150,random.randint(0,550)],
	[-200,random.randint(0,550)],
	[-250,random.randint(0,550)],
	[-300,random.randint(0,550)],
	[-350,random.randint(0,550)]
	]
	mball_pos = [350,500]
	lose_mode = False
	my_score = 0
	lose_bgcolor = [0,0,0]
lose_mode = False
paused = False
def music():
	global paused
	if paused:
		pygame.mixer.music.unpause()
	else:
		pygame.mixer.music.pause()
	paused = not paused
clock = pygame.time.Clock()
while not done:
	display.fill((255,255,255))
	if not start_menu:
		if show_help_on_start_game:
			noisyball()
			noisy3()
			pygame.draw.rect(display,[0,0,0],[200,150,400,300])
			display.blit(helpfont.render("q:", True, [0,127,0]),      (200,150)),display.blit(helpfont.render("quit", True, [0,127,0]),             (545,150))
			display.blit(helpfont.render("p:", True, [0,127,0]),      (200,180)),display.blit(helpfont.render("home page", True, [0,127,0]),        (480,180))
			display.blit(helpfont.render("k:", True, [0,127,0]),      (200,210)),display.blit(helpfont.render("move ball to up", True, [0,127,0]),  (415,210))
			display.blit(helpfont.render("i:", True, [0,127,0]),      (200,240)),display.blit(helpfont.render("move ball to down", True, [0,127,0]),(375,240))
			display.blit(helpfont.render("UPKEY:", True, [0,127,0]),  (200,270)),display.blit(helpfont.render("move ball to up", True, [0,127,0]),  (415,270))
			display.blit(helpfont.render("DOWNKEY:", True, [0,127,0]),(200,300)),display.blit(helpfont.render("move ball to down", True, [0,127,0]),(377,300))
			display.blit(helpfont.render("s:", True, [0,127,0]),      (200,330)),display.blit(helpfont.render("start/stop game", True, [0,127,0]),  (414,330))
			display.blit(helpfont.render("t:", True, [0,127,0]),      (200,360)),display.blit(helpfont.render("toggle fullscreen", True, [0,127,0]),(390,360))
			display.blit(helpfont.render("m:", True, [0,127,0]),      (200,390)),display.blit(helpfont.render("play/pause music", True, [0,127,0]), (408,390))
		else:
			if lose_mode:
				losescr()
			else:
				if not jump:
					if mball_pos[1] < 520:
						mball_pos[1] += 2
				else:
					if mball_pos[1] > 0:
						mball_pos[1] -= 2
				pygame.draw.rect(display, [255,0,0], mball_pos+[80,80])
				pygame.draw.rect(display, [0,0,255], mball_pos+[81,81],5)
				badrects()
	else:
		if adding:
			mball_rad += 1
			if mball_rad == 50:
				adding = not adding
		else: 
			mball_rad -= 1
			if mball_rad == 40:
				adding = not adding
		noisyball()
		noisy3()
		pygame.draw.circle(display, [0,0,255], [250,300], mball_rad)
		pygame.draw.circle(display, [255,255,0], [250,300], 51,5)
		display.blit(font.render("about", True, [255,255,255]),(205,290))
		pygame.draw.circle(display, [0,255,0], [400,300], mball_rad)
		pygame.draw.circle(display, [0,255,255], [400,300], 51,5)
		display.blit(font.render("start", True, [255,255,255]),(360,290))
		pygame.draw.circle(display, [255,0,0], [550,300], mball_rad)
		pygame.draw.circle(display, [255,0,255], [550,300], 51,5)
		display.blit(font.render("exit", True, [255,255,255]),(523,290))
		pygame.draw.rect(display,[0,31,31],[70,395,670,30],2)
		display.blit(font.render("press first word of button names to press it!", True, [0,0,0]),(83,400))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if start_menu:
				if event.key == pygame.K_e:
					done = True
				elif event.key == pygame.K_s:
					start_menu = not start_menu
				elif event.key == pygame.K_a:
					try:
						webbrowser.open_new_tab('https://github.com/pycdr/noisyrect')
					except:
						pass
				elif event.key == pygame.K_t:
					pygame.display.toggle_fullscreen()
				elif event.key == pygame.K_m:
					music()
			else:
				if (event.key in [pygame.K_UP,pygame.K_i]):
					jump = True
				elif (event.key in [pygame.K_DOWN,pygame.K_k]):
					jump = False
				elif (event.key in [pygame.K_LEFT,pygame.K_j]):
					if mball_pos[0] > 0:
						mball_pos[0] -= 20
				elif (event.key in [pygame.K_RIGHT,pygame.K_l]):
					if mball_pos[0] < 720:
						mball_pos[0] += 20
				elif event.key == pygame.K_q:
					done = True
				elif event.key == pygame.K_s:
					if lose_mode:
						resetgame()
					else:
						show_help_on_start_game = not show_help_on_start_game
				elif event.key == pygame.K_t:
					pygame.display.toggle_fullscreen()
				elif event.key == pygame.K_p:
					start_menu = True
				elif event.key == pygame.K_m:
					music()
	if pygame.mixer.music.get_pos() == -1:
		pygame.mixer.music.play()
	pygame.display.flip()
	clock.tick(50)
pygame.quit()
#font: http://www.fontfabric.com/lovelo-font/
#creator: pycdr (telegram,github,gitlab)
