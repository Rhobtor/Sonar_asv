// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interfaces:srv/SerialNumber.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__SERIAL_NUMBER__STRUCT_H_
#define CUSTOM_INTERFACES__SRV__DETAIL__SERIAL_NUMBER__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'serial_number'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/SerialNumber in the package custom_interfaces.
typedef struct custom_interfaces__srv__SerialNumber_Request
{
  rosidl_runtime_c__String serial_number;
} custom_interfaces__srv__SerialNumber_Request;

// Struct for a sequence of custom_interfaces__srv__SerialNumber_Request.
typedef struct custom_interfaces__srv__SerialNumber_Request__Sequence
{
  custom_interfaces__srv__SerialNumber_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__srv__SerialNumber_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/SerialNumber in the package custom_interfaces.
typedef struct custom_interfaces__srv__SerialNumber_Response
{
  bool success;
} custom_interfaces__srv__SerialNumber_Response;

// Struct for a sequence of custom_interfaces__srv__SerialNumber_Response.
typedef struct custom_interfaces__srv__SerialNumber_Response__Sequence
{
  custom_interfaces__srv__SerialNumber_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__srv__SerialNumber_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__SERIAL_NUMBER__STRUCT_H_
