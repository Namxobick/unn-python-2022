
from todo.custom_exceptions import UserExitException
from todo.models import BaseItem
from todo.reflection import find_classes


class BaseCommand(object):
    label: str

    def perform(self, store):
        raise NotImplementedError()


class ListCommand(BaseCommand):
    label = 'list'

    def perform(self, store):
        if len(store.items) == 0:
            print('There are no items in the storage.')
            return

        for index, obj in enumerate(store.items):
            print('{0}: {1}'.format(index, str(obj)))


class NewCommand(BaseCommand):
    label = 'new'

    def perform(self, store):
        classes = self._load_item_classes()

        print('Select item type:')
        for index, name in enumerate(classes.keys()):
            print('{0}: {1}'.format(index, name))

        selection = None
        selected_key = None

        while True:
            try:
                selected_key = self._select_item(classes)
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')
            else:
                break

        selected_class = classes[selected_key]
        print('Selected: {0}'.format(selected_class.__name__))
        print()

        new_object = selected_class.construct()

        store.items.append(new_object)

        print('Added {0}'.format(str(new_object)))
        print()
        return new_object

    def _load_item_classes(self) -> dict:
        # Dynamic load:
        return dict(find_classes(BaseItem))

    def _select_item(self, classes):
        selection = int(input('Input number: '))
        if selection < 0:
            raise IndexError('Index needs to be >0')
        return list(classes.keys())[selection]


class BaseMarkCommand(object):

    def perform(self, store):
        counts = 0

        for obj in store.items:
            if str(obj)[0] == self.char:
                counts += 1

        if counts == 0:
            print('There are no {0}items in the storage.'.format(self.char))
            return

        for index, obj in enumerate(store.items):
            if str(obj)[0] == self.char:
                print('{0}: {1}'.format(index, str(obj)))

        selected_item = self.select_item(store)

        print('{0} has been {1}'.format(selected_item, self.operation))
        print()

        operation = getattr(selected_item, str(self.operation), None)
        assert operation is not None
        operation()

    def select_item(self, store):
        while True:
            try:
                selection = int(input('Input number of item: '))
                if selection < 0 or str(store.items[selection])[0] != self.char:
                    raise IndexError('MarkCommand -> select_item')
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')
            else:
                break

        if store.items is None:
            print('There are no items in the storage.')
        return store.items[selection]


class DoneCommand(BaseMarkCommand, BaseCommand):
    label = 'done'
    operation = 'mark_done'
    char = '-'


class UndoneCommand(BaseMarkCommand, BaseCommand):
    label = 'undone'
    operation = 'mark_undone'
    char = '+'


class ExitCommand(BaseCommand):
    label = 'exit'

    def perform(self, _store):
        raise UserExitException('See you next time!')
