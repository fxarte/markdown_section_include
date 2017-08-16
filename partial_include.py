import os
'''
documentation: TODO
'''


if __name__=='__main__':
  # print(__doc__)
  text='''
[[include:Home## Technologies]]
[[include:Home## Application design]]  
[[include:Home## Development]]
[[include:Architecture## Modules]]
[[include:Architecture### UI navigation]]
[[include:Login## Login and access control]]
[[include:HomePage## User experience]]
[[include:MainMenu## User experience:]]

[[include:DataLayer]]

[[include:Architecture### Entities relationships]]
'''
  built=[]
  for include in text.split('\n'):
    include = include.strip()
    if not include or include.startswith('#'):
      continue
    include = include[10:-2]
    try:
      file = include[0:include.index('#')]
      section = include[include.index('#'):]
      section_end=section.index(' ')
      copy_section=False
    except:
      section_end=-1
      file = include
      section=None
      copy_section=True
    DIRBASE=''
    EXT='.md'
    with open(os.path.join(DIRBASE, file+EXT)) as f:
      page_broken=False
      if copy_section and section is not None:
        built.append("# {}".format(file))
        # print("# {}".format(file))
      for line in f:
        line=line.strip('\n')

        if copy_section:
          if line.startswith('#') and line.index(' ')<=section_end:
            copy_section=False
            built.append('<div class="page">&nbsp;</div>')
            page_broken=True
          else:
            built.append(line)
        elif section is not None:
          if line.startswith(section):
            built.append('\n')
            built.append("# {}".format(file))
            copy_section=True
            built.append(line)
            
      copy_section=False
      if not page_broken:
        built.append('<div class="page">&nbsp;</div>')
        built.append('\n')
  print('# Title')
  print("\n".join(built).strip())
