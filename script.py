import mdl
from display import *
from matrix import *
from os import remove, execlp, fork

class Script(object):

    def __init__( self ):
        self.num_frames = 1
        self.basename = "drawing"
        self.is_animated = False
        self.knobs = []

    def first_pass( self, commands ):
        found_frames = False
        found_basename = False
        for cmd in commands:
            op = cmd["op"]
            args = cmd["args"]
            if op == "frames":
                self.is_animated = True
                found_frames = True
                if not found_basename:
                    print("Set basename to '" + self.basename + "'")
                    found_basename = True
                self.num_frames = args[0]
            elif op == "basename":
                self.is_animated = True
                found_basename = True
                self.basename = args[0]
            elif op == "vary":
                self.is_animated = True
                if not found_frames:
                    print("Must call frames command before vary command")
                    return
                if not ( 0 <= args[0] < self.num_frames ) or not ( 0 <= args[1] < self.num_frames):
                    print("Must vary only existing frames")
                    return

    def second_pass( self, commands ):
        for i in range(int(self.num_frames)):
            self.knobs.append({})
        for cmd in commands:
            op = cmd["op"]
            args = cmd["args"]
##            print(str(args)+"@@@@@@@@@@@@@@@@@@")
            if op == "vary":
                knob = cmd["knob"]
                current_knob = args[2]
                step = (args[3] - args[2]) / (args[1] - args[0])
##                print(str(step)+"@@@@@")
                for i in range( int(args[0]), int(args[1])+1 ):
                    if i == int(args[1]):
                        current_knob = args[3]
                    self.knobs[i][knob] = current_knob
                    current_knob += step
##                    print(str(i)+"$$"+str(self.knobs[i])+"@@@@@@@@")

    @staticmethod
    def run( filename ):
        """
        This function runs an mdl script
        """
        script = Script()
        view = Vector([0,0,1])
        ambient_light = [100,100,100]
        light_sources = [ Light( Vector([1,1,1]).norm(), [180,20,20] ) ]
        r = [ [1,1,1],
              [1,1,1],
              [1,1,1] ]
        color = [0, 0, 0]
        coordinate_system = [Matrix.ident()]
        screen = PPMGrid()

        p = mdl.parseFile(filename)

        if p:
            (commands, symbols) = p

            script.first_pass(commands)
            script.second_pass(commands)
            print("basename: "+script.basename)
            print("number of frames: "+str(script.num_frames))
##            print(commands)
##            print(symbols)
##            print(script.num_frames)

            for frame in range(int(script.num_frames)):
                print("frame "+str(frame))

                for knob in script.knobs[frame]:
                    symbols[knob][1] = script.knobs[frame][knob]
                
                for cmd in commands:
                    e = Matrix(0,4)
                    p = Matrix(0,4)

                    if ( len(cmd) > 1 ):
                        pass
                    op = cmd["op"]
                    args = cmd["args"]
                    if not args == None:
                        args = cmd['args'][:]
                    i = 0
                    while args != None and i < len(args):
                        if ( is_number(args[i]) ):
                            args[i] = float(args[i])
                        if ( args[i] == None ):
                            args.pop(i)
                        else:
                            i += 1
                            
                    if (not args == None) and "knob" in cmd and (not cmd["knob"] == None) and op in ["move", "scale", "rotate"]:
                        knob = cmd["knob"]
                        for i in range(len(args)):
                            if not isinstance(args[i], str):
                                args[i] = args[i] * symbols[knob][1]
##                        print(str(symbols[knob][1])+"@@@@"+str(args[i]))

##                    print(args)
##                    print(coordinate_system[-1])
                    
                    if ( op == "line" ):
                        e.add_edge(*args)
                        screen.draw_lines(coordinate_system[-1]*e, color)
                    elif ( op == "ident" ):
                        t = Matrix.ident()
                    elif ( op == "scale" ):
                        coordinate_system[-1] = coordinate_system[-1] * Matrix.scaler(*args[:3])
##                        print(Matrix.scaler(*args[:3]))
##                        print(coordinate_system[-1])
                    elif ( op == "move" ):
                        coordinate_system[-1] = coordinate_system[-1] * Matrix.mover(*args[:3])
                    elif ( op == "rotate" ):
                        if ( args[0] == 'x' ):
                            coordinate_system[-1] = coordinate_system[-1] * Matrix.rotx(args[1])
                        elif ( args[0] == 'y' ):
                            coordinate_system[-1] = coordinate_system[-1] * Matrix.roty(args[1])
                        elif ( args[0] == 'z' ):
                            coordinate_system[-1] = coordinate_system[-1] * Matrix.rotz(args[1])
                    elif ( op == "apply" ):
                        e *= t
                        p *= t
                    elif ( op == "clear" ):
                        e = Matrix(0,4)
                        p = Matrix(0,4)
                        coordinate_system = [Matrix.ident()]
                        screen.clear()
                    elif ( op == "display" ):
                        screen.display()
                    elif ( op == "save" ):
                        screen.save_extension(args[0])
                    elif ( op == "quit" ):
                        return
                    elif ( op == "circle" ):
                        e.add_circle(*args)
                        screen.draw_lines(coordinate_system[-1]*e, color)
                    elif ( op == "bezier" or op == "hermite" ):
                        e.add_curve(args[0],args[1],args[2],args[3],args[4],args[5],0.001,op)
                        screen.draw_lines(coordinate_system[-1]*e, color)
                    elif ( op == "box" ):
                        p.add_box(*args)
                        p = coordinate_system[-1]*p
                        screen.draw_polygons(Prop(p,r), view, ambient_light, light_sources)
                    elif ( op == "sphere" ):
                        p.add_sphere(*args)
                        p = coordinate_system[-1]*p
##                        print(coordinate_system[-1])
                        screen.draw_polygons(Prop(p,r), view, ambient_light, light_sources)
                    elif ( op == "torus" ):
                        p.add_torus(*args)
                        p = coordinate_system[-1]*p
                        screen.draw_polygons(Prop(p,r), view, ambient_light, light_sources)
                    elif ( op == "push" ):
                        coordinate_system.append(coordinate_system[-1].copy())
                    elif ( op == "pop" ):
                        coordinate_system.pop()
                
                if script.is_animated:
                    screen.save_extension("anim/" + script.basename + ("%03d" % int(frame)) + ".png")
                    
                coordinate_system = [Matrix.ident()]
                screen = PPMGrid()

            if script.is_animated:
                script.make_animation()

        else:
            print("Parsing failed.")
            return


    def make_animation( self ):
        name = self.basename
        name_arg = 'anim/' + name + '*'
        name = name + '.gif'
        print('Saving animation as ' + name)
        f = fork()
        if f == 0:
            execlp('convert', 'convert', name_arg, name)
