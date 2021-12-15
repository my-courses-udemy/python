import facebook_snooper
from facebook_snooper.dump import dump_search, dump_info

fb = facebook_snooper.init_session()
fb.log_in('santihs.sanchez@gmail.com', 'santi123')
# <facebook_snooper.core.session.Session object at 0x10ffc58d0>

info = fb.profile_info('chars zambrana')
dump_info(info, pretty=True)