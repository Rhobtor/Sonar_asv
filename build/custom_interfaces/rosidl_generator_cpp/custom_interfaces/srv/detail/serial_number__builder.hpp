// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:srv/SerialNumber.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__SERIAL_NUMBER__BUILDER_HPP_
#define CUSTOM_INTERFACES__SRV__DETAIL__SERIAL_NUMBER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/srv/detail/serial_number__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_SerialNumber_Request_serial_number
{
public:
  Init_SerialNumber_Request_serial_number()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::srv::SerialNumber_Request serial_number(::custom_interfaces::srv::SerialNumber_Request::_serial_number_type arg)
  {
    msg_.serial_number = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::SerialNumber_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::SerialNumber_Request>()
{
  return custom_interfaces::srv::builder::Init_SerialNumber_Request_serial_number();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_SerialNumber_Response_success
{
public:
  Init_SerialNumber_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::srv::SerialNumber_Response success(::custom_interfaces::srv::SerialNumber_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::SerialNumber_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::SerialNumber_Response>()
{
  return custom_interfaces::srv::builder::Init_SerialNumber_Response_success();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__SERIAL_NUMBER__BUILDER_HPP_
