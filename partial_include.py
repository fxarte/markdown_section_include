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
  for include in text.split('\n'):
    include = include.strip()
    if not include or include.startswith('#'):
      continue
    include = include[10:-2]
    try:
      file = include[0:include.index('#')]
      section = include[include.index('#'):]
      next_section = section[:section.index(' ')]+' '
    except:
      file = include
      section=None
      next_section=None
    copy_section=False if section else True
    built=[]
    DIRBASE=''
    EXT='.md'
    with open(os.path.join(DIRBASE, file+EXT)) as f:
      page_broken=False
      if copy_section:
        built.append("# {}".format(file))
      for line in f:
        line=line.strip('\n')
        if next_section and copy_section and line.startswith(next_section):
          copy_section=False
          # Print page break
          built.append('<div class="page">&nbsp;</div>')
          page_broken=True
        elif copy_section:
          built.append(line)
        elif section and line.startswith(section):
          built.append('\n')
          built.append("# {}".format(file))
          copy_section=True
          built.append(line)
      copy_section=False
      if not page_broken:
        built.append('<div class="page">&nbsp;</div>')
        built.append('\n')
    print("\n".join(built))
