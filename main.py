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
    'category': 'Tools'
}

class OBJECT_OT_powermove(bpy.types.Operator):
    bl_idname = 'transform.powermove'
    bl_label = 'PowerMove'
    bl_options = {'REGISTER', 'UNDO'}
    prev_xy = (0, 0)

    def execute(self, context):
        return {'FINISHED'}

    def modal(self, context, event):
        # ESC will finish the operation and so will double-clicking
        if event.type == 'ESC':
            return {'FINISHED'}

        if event.type == 'LEFTMOUSE':
            print('LEFTMOUSE xy: %s, %s' % self.prev_xy)
            if (event.mouse_x, event.mouse_y) == self.prev_xy:
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
        self.prev_xy = (0, 0)
        #print('This is the invoker')
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

addon_keymaps = []
def init_keymaps():
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = [
        km.keymap_items.new('transform.powermove', type='G', value='PRESS'),
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
    global addon_keymaps
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    
    addon_keymaps.clear()
    bpy.utils.unregister_class(OBJECT_OT_powermove)

if __name__ == '__main__':
    register()
