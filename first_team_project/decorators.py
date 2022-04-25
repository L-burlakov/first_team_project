from exceptions import*


def errors_handler(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            value = func(*args, **kwargs)
            return value
        except AttributeError:
            print('Please, enter correct arguments!')
            return None
        except KeyError:
            print('Such key does not exist!')
            return None
        except IndexError:
            print('')
            return None
        except ValueError:
            print('Please, enter correct arguments!')
            return None
        except ParseException:
            print('Please, enter correct arguments!')
            return None
        except TypeError:
            print('Please, enter correct arguments!')
            return None
        except PhoneAlreadyExistsException:
            print('Such phone number already exists!')
            return None
        except NoneNameException:
            print('Please, enter name!')
            return None
        except NoSuchPhoneException:
            print('There is no such phone number in address book!')
            return None
        except EmailAlreadyExistsException:
            print('Such email already exists!')
            return None
        except NoSuchEmailException:
            print('There is no such email in address book!')
            return None
        except RecordAlreadyExistsError:
            print('Record with such contact name already exists!')
            return None
        except EmailLengthException:
            print('Length of local-part of email must be <= 64 chars!')
            return None
    return inner
