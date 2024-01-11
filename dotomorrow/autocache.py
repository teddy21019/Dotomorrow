import pickle

class SavedIterator:
    def __init__(self, file_path:str, parameter_space):
        self.__file_path = file_path
        self.__params = parameter_space
        self.__has_prev_result = False
        self.results = self.__load_results()

        self.__remaining_params = [p for p in self.__params if p not in self.results.keys()]



    def __enter__(self):
        if self.__has_prev_result:
            print(f"Cache found in {self.__file_path}. {len(self.__remaining_params)} iterations remained.")
        else:
            print("No cache file found. Staring from scratch.")
        return self

    def __exit__(self, exit_type, exit_value, trace_back):
        self.__save_results()
        self.__current_param = None
        if exit_type is KeyboardInterrupt:
            print("Interrupted. File autosaved in ", self.__file_path)
            return True


    def __load_results(self):
        try:
            with open(self.__file_path, 'rb') as file:
                self.__has_prev_result = True
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return dict()

    def __save_results(self):
        with open(self.__file_path, 'wb') as file:
            pickle.dump(self.results, file)

    def __iter__(self):
        while len(self.__remaining_params)>0:
            self.__current_param = self.__remaining_params.pop(0)
            yield self.__current_param


    def __iadd__(self, result):
        self.append(result)
        return self

    def append(self, result):
        self.results[self.__current_param] = result
        return self