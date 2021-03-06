class SemantError(Exception):
    pass


class UndefinedMethodError(SemantError):

    def __init__(self, method, _class):
        msg = 'A undefined method %s was called in class %s'
        super(UndefinedMethodError, self).__init__(msg % (method, _class))


class ReturnedTypeError(SemantError):

    def __init__(self, method, _class):
        msg = 'The method %s in class %s returns wrong type'
        super(ReturnedTypeError, self).__init__(msg % (method, _class))


class ArgumentTypeError(SemantError):

    def __init__(self, method, class_name):
        m = "Argument %s passed to method %s in class %s have a different type"
        try:
            # If is an Object, there is a name,
            content_or_name = method.name
        except AttributeError:
            # if not, there is a content instead
            content_or_name = method.content
        super(ArgumentTypeError, self).__init__(
            m % (content_or_name, method.name, class_name)
        )


class NumberOfArgumentError(SemantError):

    def __init__(self, method, _class):
        msg = 'Tried to call method %s in class %s with wrong number of arguments'
        super(NumberOfArgumentError, self).__init__(msg % (method, _class))


class RedefinedMethodError(SemantError):

    def __init__(self, method_nmae):
        msg = "Redefined method %s cannot change arguments or return type, they must be the same of the parent method"
        super(RedefinedMethodError, self).__init__(msg % (method_nmae))


class RedefinedAttributeError(SemantError):

    def __init__(self, class_nmae):
        msg = "Attribute cannot be redefined in child class %s"
        super(RedefinedAttributeError, self).__init__(msg % (class_nmae))


class UndefinedParentError(SemantError):

    def __init__(self, child, parent):
        msg = 'Classe %s inherit from an undefined parent %s'
        super(UndefinedParentError, self).__init__(msg % (child, parent))


class ClassAlreadyDefinedError(SemantError):

    def __init__(self, class_name):
        msg = 'Class %s already defined'
        super(ClassAlreadyDefinedError, self).__init__(msg % (class_name))


class InheritanceError(SemantError):

    def __init__(self, class_name):
        msg = '%s is in a inheritance cycle'
        super(InheritanceError, self).__init__(msg % (class_name))


class DeclaredTypeError(SemantError):

    def __init__(self, expression_type, value_type):
        msg = 'Let init %s is not equal to the declared type %s'
        super(DeclaredTypeError, self).__init__(
            msg % (value_type, expression_type)
        )


class AttributeTypeError(SemantError):

    def __init__(self, expression, value_type):
        msg = 'Expression %s was declared as %s and was passed %s'
        super(AttributeTypeError, self).__init__(
            msg % (expression.name, expression.type, value_type)
        )


class TypeCheckError(SemantError):

    def __init__(self, first_type, second_type, _class):
        msg = 'Must be a Integer to check with < , <= or = ! Was given %s and %s in class %s'
        super(TypeCheckError, self).__init__(
            msg % (first_type, second_type, _class.name)
        )


class EqualTypeCheckError(SemantError):

    def __init__(self, first_type, second_type, _class):
        msg = 'To compare two values, they must be String, Int or Bool. Was given %s and %s in class %s'
        super(EqualTypeCheckError, self).__init__(
            msg % (first_type, second_type, _class.name)
        )


class EqualCheckError(SemantError):

    def __init__(self, first_type, second_type, _class):
        msg = 'To compare two values, they must be the same type. Was given %s and %s in class %s'
        super(EqualCheckError, self).__init__(
            msg % (first_type, second_type, _class.name)
        )


class ArithmeticError(SemantError):

    def __init__(self, first_type, second_type, _class):
        msg = 'Arithmetic operations require integers! Was given %s and %s in class %s'
        super(ArithmeticError, self).__init__(
            msg % (first_type, second_type, _class.name)
        )


class AssignError(SemantError):

    def __init__(self, first_type, second_type, _class):
        msg = 'Assign operations require same types! Was given %s and %s in class %s'
        super(AssignError, self).__init__(
            msg % (first_type, second_type, _class.name)
        )


class ConditionStatementError(SemantError):

    def __init__(self, statement, value_type, _class):
        msg = '%s statement must have a boolean type, was given %s in class %s'
        super(ConditionStatementError, self).__init__(
            msg % (statement, value_type, _class.name)
        )
