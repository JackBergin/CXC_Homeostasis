from libpurecoollink.dyson import DysonAccount
from libpurecoollink.const import FanSpeed, FanMode, NightMode, Oscillation, \
    FanState, StandbyMonitoring, QualityTarget, ResetFilter, HeatMode, \
    FocusMode, HeatTarget

##---------------------------DEVICE CONNECTION-----------------------------------------
# Log to Dyson account
# Language is a two characters code (eg: FR)
dyson_account = DysonAccount("jbergin@ptc.com","dysonCXC2022","EN")
logged = dyson_account.login()

if not logged:
    print('Unable to login to Dyson account')
    exit(1)

# List devices available on the Dyson account
devices = dyson_account.devices()

# Connect using discovery to the first device
connected = devices[0].auto_connect()
# Manual Connection:
# connected = devices[0].connect("192.168.1.2")

# connected == device available, state values are available, sensor values are available




##---------------------------DEVICE STATE OUTPUT--------------------------------------------
print(devices[0].state.speed)
print(devices[0].state.oscillation)



##---------------------------DEVICE ENVIRONMENT OUTPUT--------------------------------------------
print(devices[0].environment_state.humidity)
print(devices[0].environment_state.sleep_timer)



##---------------------------DEVICE COMMANDS--------------------------------------------
# Turn on the fan to speed 2
devices[0].set_configuration(fan_mode=FanMode.FAN, fan_speed=FanSpeed.FAN_SPEED_2)

# Turn on oscillation
devices[0].set_configuration(oscillation=Oscillation.OSCILLATION_ON)

# Turn on night mode
devices[0].set_configuration(night_mode=NightMode.NIGHT_MODE_ON)

# Set 10 minutes sleep timer
devices[0].set_configuration(sleep_timer=10)

# Disable sleep timer
devices[0].set_configuration(sleep_timer=0)

# Set quality target (for auto mode)
devices[0].set_configuration(quality_target=QualityTarget.QUALITY_NORMAL)

# Disable standby monitoring
devices[0].set_configuration(standby_monitoring=StandbyMonitoring.STANDBY_MONITORING_OFF)

# Reset filter life
devices[0].set_configuration(reset_filter=ResetFilter.RESET_FILTER)

## Cool+Hot devices only
# Set Heat mode
devices[0].set_configuration(heat_mode=HeatMode.HEAT_ON)
# Set heat target
devices[0].set_configuration(heat_target=HeatTarget.celsius(25))
devices[0].set_configuration(heat_target=HeatTarget.fahrenheit(70))
# Set fan focus mode
devices[0].set_configuration(focus_mode=FocusMode.FOCUS_ON)



##---------------------------DEVICE DISCONNECTION--------------------------------------------
# Disconnection is required for fan/purifier devices in order 
# to release resources (an internal thread is started to request update notifications)
devices[0].disconnect()
