from datetime import datetime
import inspect

def logger_with_path(file_path):
	def logger(old_function):
		func_usage_time = "time"
		func_args = "test_args"
		func_name = "test_name"
		def new_function(stats, *args, **kwargs):
			nonlocal func_name, func_args, func_usage_time
			func_usage_time = datetime.now()
			func_name = old_function.__name__
			func_args = inspect.getfullargspec(old_function)
			old_func_result = old_function(stats, *args, **kwargs)
			log_info = f"\n\nFunction name is - {func_name}\nFunction args are - {func_args}\nFunction usage date and time is - {func_usage_time}\nFunction result is - {old_func_result}"
			with open(file_path, "a") as f:
				f.write(log_info)
			return log_info, old_func_result
		return new_function
	return logger


@logger_with_path("decorator_logs.txt")
def max_value_ad_channel(stats, *args, **kwargs):
	volumes = []
	volumes.extend(list(stats.values()))
	sorted_volumes = sorted(volumes)
	max_volume = sorted_volumes[-1]
	return max_volume



stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

max_value_ad_channel(stats)



