GlowScript 3.0 VPython
scene.autoscale = False


if __name__ == "__main__":
    button( bind=Reload, text='Reload Planets' )
    scene.append_to_caption('\n\n')
    button( bind=planet_show, text='Earth' )
    scene.append_to_caption('\t')
    button( bind=planet_show, text='Venus' )
    scene.append_to_caption('\t')
    button( bind=planet_show, text='Mars' )
    scene.append_to_caption('\t')
    button( bind=planet_show, text='Neptune' )
    scene.append_to_caption('\t\t')
    button( bind=planet_show, text='Saturn' )
    scene.append_to_caption('\t')
    button( bind=planet_show, text='Uranus' )
    scene.append_to_caption('\t')
    button( bind=planet_show, text='Mercury' )
    scene.append_to_caption('\t')
    button( bind=planet_show, text='Jupiter' )
    scene.append_to_caption('\t')
    
    scene.bind('click', run)
    
    space = sphere(pos = vector(0,0,0), texture = "https://i.imgur.com/1nVWbbd.jpg", radius = 30, shininess = 0)
    mercury_orbit = ring(axis = vector(0,1,0), pos = vector(-1.5,0,0), radius = 1.5, thickness = 0.01)
    venus_orbit = ring(axis = vector(0,1,0), pos = vector(-1.5,0,0), radius = 2.5, thickness = 0.01)
    earth_orbit = ring(axis = vector(0,1,0), pos = vector(-1.5,0,0), radius = 3.5, thickness = 0.01)
    mars_orbit = ring(axis = vector(0,1,0), pos = vector(-1.5,0,0), radius = 4.5, thickness = 0.01)
    jupiter_orbit = ring(axis = vector(0,1,0), pos = vector(-1.5,0,0), radius = 5.5, thickness = 0.01)
    saturn_orbit = ring(axis = vector(0,1,0), pos = vector(-1.5,0,0), radius = 6.5, thickness = 0.01)
    uranus_orbit = ring(axis = vector(0,1,0), pos = vector(-1.5,0,0), radius = 7.5, thickness = 0.01)
    neptune_orbit = ring(axis = vector(0,1,0), pos = vector(-1.5,0,0), radius = 8.5, thickness = 0.01)
    
    sun = sphere(pos=vector(-1.5,0,0),size = vector(2,2,2),  opacity = 1 , emissive = True, texture = "http://i.imgur.com/yoEzbtg.jpg")
    moon = sphere(pos=vector(2,0,0), size = vector(0.2,0.2,0.2), texture = "http://i.imgur.com/YPg4RPU.jpg", flipx = True, flipy = True, shininess = 0.9)
    
    mercury = sphere(pos = vector(0,0,0), size = vector(0.2,0.2,0.2),  texture = textures.wood,color = color.rgb_to_hsv(vector(0,255,255)))
    venus = sphere(pos = vector(1,0,0), size = vector(0.4,0.4,0.4),color = vector(1,1,1), texture = textures.wood)
    earth = sphere(pos = vector(2,0,0), size = vector(0.5,0.5,0.5), texture = textures.earth)
    mars = sphere(pos = vector(3,0,0), size = vector(0.3,0.3,0.3), texture = textures.wood, color = vector(1,0,0))
    jupiter = sphere(pos = vector(4,0,0),visible = True, size = vector(1.2,1.2,1.2),  color = color.orange)
    saturn = sphere(pos = vector(5,0,0), size = vector(0.8,0.8,0.8),color = color.orange, texture = textures.rough)
    uranus = sphere(pos = vector(6,0,0), size = vector(0.7,0.7,0.7), texture = textures.wood, color = color.green)
    neptune = sphere(pos = vector(7,0,0), size = vector(0.6,0.6,0.6),color = color.rgb_to_hsv(vector(255,255,0)))
    
    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
    orbits = [mercury_orbit, venus_orbit , earth_orbit , mars_orbit , jupiter_orbit , saturn_orbit , uranus_orbit , neptune_orbit]
    
    #scene.camera.follow(earth)
    t= 0
    dt = 0.5
    y0 = 2
    v0 = 0.0
    theta = 0
    thetavenus = 0
    omega = 2*pi/365



    while True:
        rate(50)
        for p in planets:
            p.rotate(angle=.01, axis=vector(0,1,0))
        planet_rev(t,dt,y0,v0,theta,omega)  
        theta = omega*t
        t+=dt
        #planet_revolution()
        #changeView()
        
    
    #rate(50)
        
    
    
    
    #rate(50)
    

def run():
    
    chosenObject = scene.mouse.pick()
    if(chosenObject!=None and chosenObject != space):
        invisible()
      # define a new function by name
        chosenObject.visible = True  # find out which object the user clicked on
        chosenObject.size = vector(7,7,7)
        scene.camera.follow(chosenObject)
        
        
    

        
def planet_rev(t,dt,y0,v0,theta,omega):
    rate(50)
    #print("hello")
    x = (1.5)*cos(omega*(t+50)) 
    y = (1.5)*sin(omega*(t+50))
    
    mercury.pos = vector(y-1.5,0,x)
        
    x = (2.5)*cos(omega*(t+100))
    y = (2.5)*sin(omega*(t+100))
    venus.pos = vector(y-1.5,0,x)
    
    x = (3.5)*cos(omega*(t+300))
    y = (3.5)*sin(omega*(t+300))
    moon.pos = vector(y-0.5,0,x)
    earth.pos = vector(y-1.5,0,x)
    
    x = (4.5)*cos(omega*(t+200))
    y = (4.5)*sin(omega*(t+200))
    mars.pos = vector(y-1.5,0,x)
    
    
    x = (5.5)*cos(omega*(t+400))
    y = (5.5)*sin(omega*(t+400))
    jupiter.pos = vector(y-1.5,0,x)
    
    
    x = (6.5)*cos(omega*(t+150))
    y = (6.5)*sin(omega*(t+150))
    saturn.pos = vector(y-1.5,0,x)
    
    
    x = (7.5)*cos(omega*(t+350))
    y = (7.5)*sin(omega*(t+350))
    uranus.pos = vector(y-1.5,0,x)
    
    
    x = (8.5)*cos(omega*(t+250))
    y = (8.5)*sin(omega*(t+250))
    neptune.pos = vector(y-1.5,0,x)
    

def Reload(b):
    #print("helo")
    
    #print("")
    #$('<script> document.getElementById("text"). value = "" </script>')
    for p in planets:
        p.visible = True
           
    moon.visible = True        
    sun.visible = True
            
    for o in orbits:
        o.visible = True
      
    scene.camera.follow(None)
    moon.size = vector(0.2,0.2,0.2)
    mercury.size = vector(0.2,0.2,0.2)
    earth.size = vector(0.5,0.5,0.5)
    sun.size = vector(2,2,2)
    venus.size = vector(0.4,0.4,0.4)
    mars.size = vector(0.3,0.3,0.3)
    jupiter.size = vector(0.9,0.9,0.9)
    saturn.size = vector(0.8,0.8,0.8)
    uranus.size = vector(0.7,0.7,0.7)
    neptune.size = vector(0.6,0.6,0.6)


def planet_show(b):
    if(b.text == "Earth"):
        invisible()
        earth.visible = True
        earth.size = vector(7,7,7)
        scene.camera.follow(earth)
        print("Earth is the planet where everyone lives")
    elif (b.text == "Venus"):
        invisible()
        venus.visible = True
        scene.camera.follow(venus)
        venus.size = vector(7,7,7)
    elif (b.text == "Jupiter"):
        invisible()
        jupiter.visible = True
        scene.camera.follow(jupiter)
        jupiter.size = vector(7,7,7)
    elif (b.text == "Saturn"):
        invisible()
        saturn.visible = True
        scene.camera.follow(saturn)
        saturn.size = vector(7,7,7)
    elif(b.text == "Uranus"):
        invisible()
        uranus.visible = True
        scene.camera.follow(uranus)
        uranus.size = vector(7,7,7)
    elif(b.text == "Neptune"):
        invisible()
        neptune.visible = True
        scene.camera.follow(neptune)
        neptune.size = vector(7,7,7)
    elif(b.text == "Mercury"):
        invisible()
        mercury.visible = True
        scene.camera.follow(mercury)
        mercury.size = vector(7,7,7)
    else:
        invisible()
        mars.visible = True
        scene.camera.follow(mars)
        mars.size = vector(7,7,7)
        
        
    



def invisible():
    for p in planets:
        p.visible = False
       
    moon.visible = False
    sun.visible = False
    
    for o in orbits:
        o.visible = False
