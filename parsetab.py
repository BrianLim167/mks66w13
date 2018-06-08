
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMBIENT BASENAME BOX CAMERA CO COMMENT CONSTANTS DISPLAY DOUBLE FOCAL FRAMES GENERATE_RAYFILES ID INT LIGHT LINE MESH MOVE POP PUSH ROTATE SAVE SAVE_COORDS SAVE_KNOBS SCALE SCREEN SET SET_KNOBS SHADING SHADING_TYPE SPHERE STRING TEXTURE TORUS TWEEN VARY WEB XYZinput :\n            | command inputcommand : COMMENTSYMBOL : XYZ\n              | IDTEXT : SYMBOL\n            | STRINGNUMBER : DOUBLEcommand : POP\n                 | PUSHcommand : SCREEN INT INT\n                 | SCREENcommand : SAVE TEXT TEXTcommand : DISPLAYcommand : SPHERE NUMBER NUMBER NUMBER NUMBER\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER\n               | SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : TORUS NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOLcommand : MOVE NUMBER NUMBER NUMBER SYMBOL\n               | MOVE NUMBER NUMBER NUMBERcommand : SCALE NUMBER NUMBER NUMBER SYMBOL\n                 | SCALE NUMBER NUMBER NUMBERcommand : ROTATE XYZ NUMBER SYMBOL\n                 | ROTATE XYZ NUMBERcommand : FRAMES INTcommand : BASENAME TEXTcommand : VARY SYMBOL INT INT NUMBER NUMBERcommand : SET SYMBOL NUMBER\n               | SET_KNOBS NUMBERcommand : AMBIENT INT INT INTcommand : CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : LIGHT SYMBOL NUMBER NUMBER NUMBER INT INT INTcommand : SHADING SHADING_TYPEcommand : CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : GENERATE_RAYFILEScommand : MESH CO TEXT\n               | MESH SYMBOL CO TEXT\n               | MESH CO TEXT SYMBOL\n               | MESH SYMBOL CO TEXT SYMBOLcommand : SAVE_KNOBS SYMBOLcommand : SAVE_COORDS SYMBOLcommand : TWEEN NUMBER NUMBER SYMBOL SYMBOLcommand : FOCAL NUMBERcommand : WEBcommand : TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER'
    
_lr_action_items = {'CONSTANTS':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[2,-14,-52,-3,-9,-61,2,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'XYZ':([2,4,5,10,12,15,16,18,20,22,23,24,29,32,33,35,37,38,41,42,44,59,73,74,77,81,95,96,98,100,107,126,127,136,143,148,151,152,161,164,166,172,],[38,38,38,38,38,38,38,56,38,38,38,38,38,38,38,-8,-5,-4,38,-6,-7,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'SCALE':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[3,-14,-52,-3,-9,-61,3,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'MESH':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[4,-14,-52,-3,-9,-61,4,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'CO':([4,37,38,40,],[41,-5,-4,73,]),'ID':([2,4,5,10,12,15,16,20,22,23,24,29,32,33,35,37,38,41,42,44,59,73,74,77,81,95,96,98,100,107,126,127,136,143,148,151,152,161,164,166,172,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,-8,-5,-4,37,-6,-7,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'BASENAME':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[5,-14,-52,-3,-9,-61,5,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'AMBIENT':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[7,-14,-52,-3,-9,-61,7,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'MOVE':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[6,-14,-52,-3,-9,-61,6,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'TWEEN':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[8,-14,-52,-3,-9,-61,8,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SCREEN':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[30,-14,-52,-3,-9,-61,30,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SAVE_KNOBS':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[10,-14,-52,-3,-9,-61,10,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'CAMERA':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[1,-14,-52,-3,-9,-61,1,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'GENERATE_RAYFILES':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[19,-14,-52,-3,-9,-61,19,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'VARY':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[12,-14,-52,-3,-9,-61,12,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'LINE':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[23,-14,-52,-3,-9,-61,23,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'DISPLAY':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[14,-14,-52,-3,-9,-61,14,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SAVE_COORDS':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[15,-14,-52,-3,-9,-61,15,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'BOX':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[16,-14,-52,-3,-9,-61,16,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'INT':([7,11,30,35,37,38,46,50,67,76,78,129,144,157,],[46,49,67,-8,-5,-4,76,78,90,99,101,144,157,167,]),'SHADING':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[17,-14,-52,-3,-9,-61,17,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'ROTATE':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[18,-14,-52,-3,-9,-61,18,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'TORUS':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[20,-14,-52,-3,-9,-61,20,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'COMMENT':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[21,-14,-52,-3,-9,-61,21,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SAVE':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[22,-14,-52,-3,-9,-61,22,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'DOUBLE':([1,3,6,8,13,16,20,23,24,28,34,35,36,37,38,39,45,47,53,54,56,57,58,60,61,62,63,66,68,69,70,71,72,75,79,80,82,83,85,86,87,88,89,91,93,94,101,102,103,105,106,107,108,109,110,111,112,113,114,119,120,121,122,123,124,125,126,128,130,131,132,134,135,137,138,139,140,141,145,147,149,153,154,155,158,159,165,168,169,174,175,177,178,179,180,181,182,183,],[35,35,35,35,35,35,35,35,35,35,35,-8,35,-5,-4,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'FRAMES':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[11,-14,-52,-3,-9,-61,11,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'FOCAL':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[13,-14,-52,-3,-9,-61,13,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'$end':([0,9,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,64,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[-1,0,-14,-52,-3,-9,-61,-1,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-2,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SHADING_TYPE':([17,],[55,]),'SPHERE':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[24,-14,-52,-3,-9,-61,24,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'POP':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[25,-14,-52,-3,-9,-61,25,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'WEB':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[26,-14,-52,-3,-9,-61,26,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SET_KNOBS':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[28,-14,-52,-3,-9,-61,28,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'LIGHT':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[29,-14,-52,-3,-9,-61,29,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'STRING':([5,22,37,38,41,42,44,59,73,],[44,44,-5,-4,44,-6,-7,44,44,]),'PUSH':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[31,-14,-52,-3,-9,-61,31,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'TEXTURE':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[32,-14,-52,-3,-9,-61,32,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),'SET':([0,14,19,21,25,26,27,30,31,35,37,38,42,43,44,48,49,51,52,55,65,74,81,84,90,92,95,96,97,98,99,104,115,116,117,118,127,133,136,142,143,146,148,150,151,152,156,160,161,162,163,164,166,167,170,171,172,173,176,178,184,185,],[33,-14,-52,-3,-9,-61,33,-12,-10,-8,-5,-4,-6,-42,-7,-57,-41,-60,-58,-50,-45,-53,-40,-13,-11,-44,-38,-54,-55,-36,-46,-39,-37,-56,-35,-59,-15,-43,-19,-17,-16,-51,-23,-20,-21,-27,-18,-24,-25,-22,-28,-29,-31,-49,-26,-30,-33,-32,-34,-47,-48,-62,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'NUMBER':([1,3,6,8,13,16,20,23,24,28,34,36,39,45,47,53,54,56,57,58,60,61,62,63,66,68,69,70,71,72,75,79,80,82,83,85,86,87,88,89,91,93,94,101,102,103,105,106,107,108,109,110,111,112,113,114,119,120,121,122,123,124,125,126,128,130,131,132,134,135,137,138,139,140,141,145,147,149,153,154,155,158,159,165,168,169,174,175,177,178,179,180,181,182,183,],[34,39,45,47,51,53,57,60,62,65,70,71,72,75,77,79,80,81,82,83,85,86,87,88,89,91,92,93,94,95,98,102,103,105,106,107,108,109,110,111,112,113,114,119,120,121,122,123,124,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,143,145,146,147,148,149,151,152,153,154,155,158,159,161,164,165,166,168,169,172,174,175,177,178,179,180,181,182,183,184,185,]),'SYMBOL':([2,4,5,10,12,15,16,20,22,23,24,29,32,33,41,59,73,74,77,81,95,96,98,100,107,126,127,136,143,148,151,152,161,164,166,172,],[36,40,42,48,50,52,54,58,42,61,63,66,68,69,42,42,42,97,100,104,115,116,117,118,125,140,142,150,156,160,162,163,170,171,173,176,]),'input':([0,27,],[9,64,]),'TEXT':([5,22,41,59,73,],[43,59,74,84,96,]),'command':([0,27,],[27,27,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> input","S'",1,None,None,None),
  ('input -> <empty>','input',0,'p_input','mdl.py',122),
  ('input -> command input','input',2,'p_input','mdl.py',123),
  ('command -> COMMENT','command',1,'p_command_comment','mdl.py',127),
  ('SYMBOL -> XYZ','SYMBOL',1,'p_SYMBOL','mdl.py',131),
  ('SYMBOL -> ID','SYMBOL',1,'p_SYMBOL','mdl.py',132),
  ('TEXT -> SYMBOL','TEXT',1,'p_TEXT','mdl.py',136),
  ('TEXT -> STRING','TEXT',1,'p_TEXT','mdl.py',137),
  ('NUMBER -> DOUBLE','NUMBER',1,'p_NUMBER','mdl.py',141),
  ('command -> POP','command',1,'p_command_stack','mdl.py',145),
  ('command -> PUSH','command',1,'p_command_stack','mdl.py',146),
  ('command -> SCREEN INT INT','command',3,'p_command_screen','mdl.py',150),
  ('command -> SCREEN','command',1,'p_command_screen','mdl.py',151),
  ('command -> SAVE TEXT TEXT','command',3,'p_command_save','mdl.py',158),
  ('command -> DISPLAY','command',1,'p_command_show','mdl.py',162),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER','command',5,'p_command_sphere','mdl.py',166),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_sphere','mdl.py',167),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL','command',6,'p_command_sphere','mdl.py',168),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_sphere','mdl.py',169),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_torus','mdl.py',173),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_torus','mdl.py',174),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_torus','mdl.py',175),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_torus','mdl.py',176),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_box','mdl.py',180),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_box','mdl.py',181),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_box','mdl.py',182),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_box','mdl.py',183),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_line','mdl.py',187),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_line','mdl.py',188),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',189),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',190),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',191),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',192),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',9,'p_command_line','mdl.py',193),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',10,'p_command_line','mdl.py',194),
  ('command -> MOVE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_move','mdl.py',198),
  ('command -> MOVE NUMBER NUMBER NUMBER','command',4,'p_command_move','mdl.py',199),
  ('command -> SCALE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_scale','mdl.py',207),
  ('command -> SCALE NUMBER NUMBER NUMBER','command',4,'p_command_scale','mdl.py',208),
  ('command -> ROTATE XYZ NUMBER SYMBOL','command',4,'p_command_rotate','mdl.py',216),
  ('command -> ROTATE XYZ NUMBER','command',3,'p_command_rotate','mdl.py',217),
  ('command -> FRAMES INT','command',2,'p_command_frames','mdl.py',225),
  ('command -> BASENAME TEXT','command',2,'p_command_basename','mdl.py',229),
  ('command -> VARY SYMBOL INT INT NUMBER NUMBER','command',6,'p_command_vary','mdl.py',233),
  ('command -> SET SYMBOL NUMBER','command',3,'p_command_knobs','mdl.py',238),
  ('command -> SET_KNOBS NUMBER','command',2,'p_command_knobs','mdl.py',239),
  ('command -> AMBIENT INT INT INT','command',4,'p_command_ambient','mdl.py',245),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',11,'p_command_constants','mdl.py',249),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_command_constants','mdl.py',250),
  ('command -> LIGHT SYMBOL NUMBER NUMBER NUMBER INT INT INT','command',8,'p_command_light','mdl.py',254),
  ('command -> SHADING SHADING_TYPE','command',2,'p_command_shading','mdl.py',258),
  ('command -> CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_camera','mdl.py',262),
  ('command -> GENERATE_RAYFILES','command',1,'p_command_generate_rayfiles','mdl.py',266),
  ('command -> MESH CO TEXT','command',3,'p_command_mesh','mdl.py',270),
  ('command -> MESH SYMBOL CO TEXT','command',4,'p_command_mesh','mdl.py',271),
  ('command -> MESH CO TEXT SYMBOL','command',4,'p_command_mesh','mdl.py',272),
  ('command -> MESH SYMBOL CO TEXT SYMBOL','command',5,'p_command_mesh','mdl.py',273),
  ('command -> SAVE_KNOBS SYMBOL','command',2,'p_save_knobs','mdl.py',277),
  ('command -> SAVE_COORDS SYMBOL','command',2,'p_save_coords','mdl.py',281),
  ('command -> TWEEN NUMBER NUMBER SYMBOL SYMBOL','command',5,'p_tween','mdl.py',286),
  ('command -> FOCAL NUMBER','command',2,'p_focal','mdl.py',290),
  ('command -> WEB','command',1,'p_web','mdl.py',294),
  ('command -> TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_texture','mdl.py',298),
]