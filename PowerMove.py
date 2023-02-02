import bpy

bl_info = {
    'name': 'PowerMove',
    'description': 'PowerMove is a tool for rapid animation',
    'author': 'Hanan Beer',
    'version': (1, 0),
    'blender': (2, 65, 0),
    'location': 'View3D',
    #'warning': '', # used for warning icon and text in addons panel
    #'doc_url': '',
    #'tracker_url': '',
    #'support': '',
    'category': 'Animation'
}

OP_PowerMove = 'transform.powermove'

class OBJECT_OT_powermove(bpy.types.Operator):
    bl_idname = OP_PowerMove
    bl_label = 'PowerMove'
    bl_options = {'REGISTER', 'UNDO'}
    prev_xy = (0, 0)
    is_running = False

    # TODO: don't need to limit just to pose mode
    # but for the initial version let's experiment just in pose
    # (remember to restore bl_idname above to transform.powermove)
    # @classmethod
    # def poll(cls, context):
    #     return (context.object and
    #             context.mode == 'POSE' and
    #             context.object.pose)

    def execute(self, context):
        return {'FINISHED'}

    def modal(self, context, event):
        # detect out-of-bounds in case switching areas, e.g. user moves to timeline
        if event.mouse_x < context.area.x or event.mouse_x > context.area.x + context.area.width or event.mouse_y < context.area.y or event.mouse_y > context.area.y + context.area.height:
           print('oob')
           OBJECT_OT_powermove.is_running = False
           return {'FINISHED'}

        # ESC will finish the operation and so will double-clicking
        if event.type == 'ESC':
            OBJECT_OT_powermove.is_running = False
            return {'FINISHED'}

        if event.type == 'LEFTMOUSE':
            if (event.mouse_x, event.mouse_y) == self.prev_xy:
                OBJECT_OT_powermove.is_running = False
                return {'FINISHED'}
        
            # allow selecting different objects/bones when pressing alt by returning PASS_THROUGH instead
            if not event.alt:
                self.prev_xy = (event.mouse_x, event.mouse_y)
                bpy.ops.transform.translate('INVOKE_DEFAULT')
                #return {'PASS_THROUGH'}
        elif event.type == 'RIGHTMOUSE':
            # right mouse to rotate, combine with alt to trackball
            if event.alt:
                bpy.ops.transform.trackball('INVOKE_DEFAULT')
            else:
                bpy.ops.transform.rotate('INVOKE_DEFAULT')

            # prevent context menu from opening on right click
            return {'RUNNING_MODAL'}

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        # prevent running operator multiple times (e.g. pressing 'G' while operator running)
        if OBJECT_OT_powermove.is_running:
            return {'CANCELLED'}

        OBJECT_OT_powermove.is_running = True
        self.prev_xy = (0, 0)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

addon_keymaps = []
def init_keymaps():
    kc = bpy.context.window_manager.keyconfigs.addon
    # TODO: currently limiting keymap only to pose, but you can still invoke via transform.powermove 
    km = kc.keymaps.new(name='Pose')
    kmi = [
        km.keymap_items.new(OP_PowerMove, type='G', value='PRESS'),
    ]
    return km, kmi

def register():
    global addon_keymaps
    bpy.utils.register_class(OBJECT_OT_powermove)
    
    if not bpy.app.background:
        km, kmi = init_keymaps()
        for k in kmi:
            k.active = True
            addon_keymaps.append((km, k))

def unregister():
    # TODO: figure out why blender (3.1) does not call unregister...
    print('unreg')
    global addon_keymaps
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    
    addon_keymaps.clear()
    bpy.utils.unregister_class(OBJECT_OT_powermove)

register()
